import random

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QListWidgetItem, QCalendarWidget, QTableWidget, QTableWidgetItem, QListWidget
from PyQt5.QtCore import Qt, QTime, QDate
from PyQt5.QtGui import QPixmap, QBrush, QColor

# связываемся с содержимым папки exceptions
from exceptions import DatabaseException, MyException
# связываемся с содержимым папки utility
from utility import *
# связываемся с содержимым папки gui
from gui import *


class MyWin(QtWidgets.QMainWindow):
    """контроллер главного окна"""
    current_selected_date = None
    selected_week_notes = None
    last_selected_date = None

    def __init__(self, parent=None):

        try:
            QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Window)
            # загрузка графического интерфейса
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            # связывание нажатие на кнопку мыши с соответствующими кнопками в органайзере
            self.ui.openNewNoteButton.clicked.connect(self.open_new_note_window)
            self.ui.listWidget.itemClicked.connect(self.list_widget_item_click)
            self.ui.calendarWidget.selectionChanged.connect(self.selected_date)
            # self.ui.tableWidget.pressed.connect(self.selected_item)
            # присваиваем переменной тип MyDate()
            MyWin.current_selected_date = MyDate()
            # присваиваем ей дату, выбранную на календаре
            MyWin.current_selected_date.set_qt_date(self.ui.calendarWidget.selectedDate())
            # создаем объект, в котором будет находииться контроллер для добавления заметок
            self.new_note_window = NewNoteController(parent=self, date=self.ui.calendarWidget.selectedDate())
            # загрузка заметок за текущую неделю
            self.load_current_week_notes(MyWin.current_selected_date)
            # загрузка заметок за текущий день
            self.load_current_day_notes(MyWin.current_selected_date)
            # создаём объект, в котором будет находиться контроллер для напоминания о выполнении приближающихся задач
            dead_line = DeadLineController(MyWin.current_selected_date, self)
            dead_line.show()
        # отображение ошибок
        except MyException as e:
            logger.log_exception(e)
            ErrorWindowController(str(e), self)
            QtCore.QTimer.singleShot(2000,  self.close)
        except Exception as e:
            logger.log_exception(e)
            ErrorWindowController("Возникла ошибка при открытии приложения!", self)
            # закрытие окна через 2 секунды
            QtCore.QTimer.singleShot(2000, self.close)

    def selected_date(self):
        """обработка нажатия на календарь"""
        try:
            # перезаписываем выбранную и предыдущую даты
            MyWin.last_selected_date = MyWin.current_selected_date
            # обновляем текущую дату
            MyWin.current_selected_date = MyDate()
            MyWin.current_selected_date.set_qt_date(self.ui.calendarWidget.selectedDate())
            # временные переменные, чтобы не таскать в if огромные названия
            cur = MyWin.current_selected_date
            last = MyWin.last_selected_date
            # проверка - новая дата находится на той же неделе, что и предыдущая или нет
            if cur.get_number_of_week() != last.get_number_of_week() or cur.get_year() != last.get_year():
                # очистка массивов
                for i in MyWin.selected_week_notes:
                    i.clear()
                # очистка таблицы
                self.clean_table()
                # загрузка массивов, соответсвующей номеру недели, в которой находится выбранная дата
                self.load_current_week_notes(cur)
            # проверка - выбрана новая дата или же осталась старая
            if cur != last:
                # загрузка заметок за текущий день
                self.load_current_day_notes(cur)
        # отображение ошибок
        except MyException as e:
            logger.log_exception(e)
            ErrorWindowController(str(e), self)

    def open_new_note_window(self):
        """обработка нажатия на кнопку добавления задачи"""
        self.new_note_window.set_date(self.ui.calendarWidget.selectedDate())
        self.new_note_window.show()

    def list_widget_item_click(self, item: QListWidgetItem):
        """обработка нажатия на элемент listWidget, где находятся задачи на текущий день"""
        # записываем в переменную данные, которые лежат в ячейке
        selected_note = item.data(Qt.UserRole)
        # вызываем окно для редактирования заметки
        NoteEditorController(selected_note=selected_note, main_window=self)


    def clean_table(self):
        """данная функция перекрашивает таблицу в белый цвет"""
        for cell_row in range(96):
            for cell_column in range(7):
                item = QtWidgets.QTableWidgetItem()
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                item.setBackground(brush)
                self.ui.tableWidget.setItem(cell_row, cell_column, item)

    def load_current_week_notes(self, cur: MyDate):
        """данная функция загружает заметки в массив и раскрашивает таблицу"""
        # cur - выбранная дата, по ней определяется номер недели и загружаются заметки за эту неделю
        MyWin.selected_week_notes = NoteLoader.load_notes_by_week_number(selected_date=cur)
        #  раскрашиваем таблицу
        for array_of_notes in MyWin.selected_week_notes:
            # array_of_notes - массив с заметками одного дня
            for element in array_of_notes:
                # получаем позицию начальной ячейки
                cell_row, cell_column = NewNoteController.get_row_col(element.get_start(), element.get_date(), False)
                # получаем позицию последней ячейки
                cell_row_end, cell_column_end = NewNoteController.get_row_col(
                                                                element.get_end(), element.get_date(), True)
                MyWin.colorize_table(self.ui.tableWidget, element, cell_row, cell_column, cell_row_end)

    def load_current_day_notes(self, cur: MyDate):
        """данная функция загружает заметки за выбранный день в listWidget"""
        # cur - выбранная дата
        notes = MyWin.selected_week_notes[cur.get_number_of_day()]
        # очищаем listWidget
        self.ui.listWidget.clear()
        # сортируем заметки по времени
        notes = sorted(notes, key=Note.get_start)
        for i in notes:
            # создаём новую дату
            item = QListWidgetItem()
            # загружаем дату по ключу Qt.UserRole
            item.setData(Qt.UserRole, i)
            # загружаем текст
            item.setText(str(i))
            # добавляем в listWidget созданную ячейку
            self.ui.listWidget.addItem(item)

    def refresh_window(self):
        """функция очищает таблицу и окошко с заметками текущего дня"""
        try:
            self.clean_table()
            self.ui.listWidget.clear()
            # загрузка обновлённых данных, в которых уже нет удаленной заметки
            self.load_current_week_notes(MyWin.current_selected_date) # за текущий день
            self.load_current_day_notes(MyWin.current_selected_date) # за текущую неделю
        # отображение ошибок
        except MyException as e:
            logger.log_exception(e)
            ErrorWindowController(str(e), self)

    @staticmethod
    def colorize_table(table: QTableWidget, n: Note, cell_row: int, cell_column: int, cell_row_end: int):
        """функция раскрашивает таблицу"""
        # красим ячейки от первой до последней
        while cell_row < cell_row_end:
            # item - новая ячейка
            item = QtWidgets.QTableWidgetItem()
            old_item = QTableWidgetItem(table.item(cell_row, cell_column))
            old_color = QColor(old_item.background().color())
            # brush - цвет новой ячейки
            brush = None
            if n.is_important():
                brush = QBrush(QColor(255, 19, 74))
            # если ячейка не красная или белая
            elif old_color.red() != 255 or (old_color.green() == 255 and old_color.blue() == 255
                                            and old_color.red() == 255):
                brush = QBrush(QColor(19, 255, 74))
            # QtCore.Qt.Dense4Pattern - позволяет красить ячейку в крапинку
            if brush is not None:
                brush.setStyle(QtCore.Qt.Dense4Pattern)
                item.setBackground(brush)
                table.setItem(cell_row, cell_column, item)
            cell_row += 1


class NewNoteController(QtWidgets.QDialog):
    """контроллер окна добавления заметки"""
    def __init__(self, date: QCalendarWidget, parent: MyWin):
        try:
            # создаём диалоговое окно
            QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Dialog)
            self.parent = parent
            self.date = date
            self.ui = Ui_NewTaskForm()
            self.ui.setupUi(self)
            self.ui.add_note_button.clicked.connect(self.add_note_btn_click)
        # вывод ошибок на экран
        except Exception as e:
            logger.log_exception(e)
            ErrorWindowController("Не удалось открыть окно добавления заметок", self)

    def add_note_btn_click(self):
        """обработка нажатия на кнопку добавления заметки"""
        try:
            # заводим переменную, отвечающую за то, является ли задача важной или нет
            # принимает два значения - 0 и 1
            # 0 - нет нажатия на important_check_box.checkState()
            # 1 - есть нажатие
            important = int(self.ui.important_check_box.checkState() == Qt.Checked)
            # в заметку n передаётся информация о времени начала, окончания, даты, названия, текста, степени важности
            n = Note(MyTime(s=self.ui.start_spinner.text()),
                     MyTime(s=self.ui.end_spinner.text()),
                     MyDate(date=self.date),
                     self.ui.title_line_edit.text(),
                     self.ui.description_text_panel.toPlainText(),
                     important
                     )
            try:
                # сравниваем заметку n с массивом заметоками дня, в который мы хотим добавить заметку,
                # чтобы выяснить, нет ли перекрытия по времени
                NoteComparator.compare_note_with_array(n, self.parent.selected_week_notes[MyDate(self.date).get_number_of_day()])
                # загружаем заметку
                NoteLoader.upload(n)
                self.parent.refresh_window()
                self.hide()
            except DatabaseException as e:
                logger.log_exception(e)
                ErrorWindowController(str(e), self)
        except MyException as e:
            logger.log_exception(e)
            ErrorWindowController(str(e), self)
        except Exception as e:
            logger.log_exception(e)
            ErrorWindowController("Не удалось добавить заметку", self)

    def set_date(self, date: QCalendarWidget):
        """функция для установки даты заметки"""
        self.date = date

    @staticmethod
    def get_row_col(time: MyTime, date: MyDate, is_end: bool):
        """данный метод возвращает позицию ячейки исходя из времени и даты"""
        hours = time.hour()
        minutes = time.minute()
        cell_row = hours * 4 + minutes // 15
        # если остаток от деления отличен от нуля, то закрашивается и следующая ячейка
        if is_end and minutes % 15 != 0:
            cell_row += 1
        cell_column = date.get_number_of_day()
        return cell_row, cell_column


class DeadLineController(QtWidgets.QDialog):
    """контроллер окна с ближайшими задачами"""
    def __init__(self, cur: MyDate, parent: MyWin=None):
        try:
            QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Dialog)
            self.parent = parent
            self.ui = Ui_Deadline()
            self.ui.setupUi(self)
            self.cur = cur
            self.ui.listWidget.itemClicked.connect(self.item_clicked)
            # загружаем заметки за текущий день и за следующий
            self.update_list_widget()
        except MyException as ex:
            logger.log_exception(ex)
            ErrorWindowController(str(ex), self)
        except Exception as e:
            logger.log_exception(e)
            ErrorWindowController("Не удалось загрузить ближайшие задачи!", self)

    def item_clicked(self, item: QListWidgetItem):
        selected_note = item.data(Qt.UserRole)
        NoteEditorController(selected_note=selected_note, main_window=self.parent, parent=self)

    def update_list_widget(self):
        self.ui.listWidget.clear()
        for i in (NoteLoader.load_notes_by_day(self.cur) + NoteLoader.load_notes_by_day(self.cur.get_next_day())):
            item = QListWidgetItem()
            item.setData(Qt.UserRole, i)
            item.setText(str(i))
            self.ui.listWidget.addItem(item)


class NoteEditorController(QtWidgets.QDialog):
    """контроллер окна редактирования заметок"""
    def __init__(self, selected_note: Note, main_window: MyWin = None, parent: DeadLineController = None):
        try:
            # создаём диалоговое окно
            QtWidgets.QWidget.__init__(self, main_window, flags=QtCore.Qt.Dialog)
            self.parent = parent
            self.main_window = main_window
            self.note = selected_note
            self.ui = Ui_NoteEditor()
            self.ui.setupUi(self)
            # заполняем графические элементы данными заметки
            self.ui.title_line_edit.setText(selected_note.get_title())
            self.ui.description_text_panel.setPlainText(selected_note.get_description())
            self.ui.start_spinner.setTime(QTime(selected_note.get_start().hour(), selected_note.get_start().minute()))
            self.ui.end_spinner.setTime(QTime(selected_note.get_end().hour(), selected_note.get_end().minute()))
            self.ui.important_check_box.setChecked(self.note.is_important())
            # получаем дату
            self.date = selected_note.get_date()
            # связываем кнопочки с соответствующими функциями
            self.ui.delete_note_button.clicked.connect(self.delete_button_click)
            self.ui.save_button.clicked.connect(self.save_button_click)
            self.ui.change_date_button.clicked.connect(self.change_date)
            self.show()
        # вывод ошибок на экран
        except Exception as e:
            logger.log_exception(e)
            ErrorWindowController("Не удалось открыть окно редактирования заметок", self)

    def refresh_main_window_and_parent(self):
        """функция, которая вызывает перерисовку главного окна"""
        self.main_window.refresh_window()
        if self.parent is not None:
            self.parent.update_list_widget()

    def delete_button_click(self):
        """обработка нажатия на кнопку удаления заметки"""
        NoteDeleteController(selected_note=self.note, parent=self)

    def save_button_click(self):
        """обработка нажатия на кнопку сохранения заметки"""
        try:
            # загружаем заметки текущего дня
            array = NoteLoader.load_notes_by_day(self.date)
            # заводим переменную, отвечающую за то, является ли задача важной или нет
            # принимает два значения - 0 и 1
            # 0 - нет нажатия на important_check_box.checkState()
            # 1 - есть нажатие
            important = int(self.ui.important_check_box.checkState() == Qt.Checked)
            # в заметку n передаётся информация о времени начала, окончания, даты, названия, текста, степени важности
            n = Note(MyTime(s=self.ui.start_spinner.text()),
                     MyTime(s=self.ui.end_spinner.text()),
                     self.date,
                     self.ui.title_line_edit.text(),
                     self.ui.description_text_panel.toPlainText(),
                     important
                     )
            # удаляем старую заметку
            for i in array:
                if i == self.note:
                    array.remove(i)
            # сравниваем заметку с заметками массива на предмет перекрытия по времени
            NoteComparator.compare_note_with_array(n, array)
            # удаляем заметку
            NoteLoader.delete(self.note)
            # загружаем заметку
            NoteLoader.upload(n)
            # закрываем окно
            self.hide()
            self.refresh_main_window_and_parent()
        except MyException as ex:
            logger.log_exception(ex)
            ErrorWindowController(str(ex), self)
        except Exception as e:
            logger.log_exception(e)
            ErrorWindowController("Не удалось сохранить заметку", self)

    def change_date(self):
        """обработка нажатия на кнопку изменения даты"""
        CalendarWindowController(self.date, parent=self)


class NoteDeleteController(QtWidgets.QDialog):
    """контроллер окна удаления заметки"""
    def __init__(self, selected_note: Note, parent: NoteEditorController):
        try:
            QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Dialog)
            self.parent = parent
            self.note = selected_note
            self.ui = Ui_DeleteNote()
            self.ui.setupUi(self)
            self.ui.ok_button.clicked.connect(self.delete_button_click)
            self.show()
        except Exception as e:
            logger.log_exception(e)
            ErrorWindowController("Не удалось открыть окно удаления заметки", self)

    def delete_button_click(self):
        """обработка нажатия на кнопку ОК"""
        try:
            NoteLoader.delete(self.note)
            self.hide()
            self.parent.refresh_main_window_and_parent()
            self.parent.hide()
        except MyException as ex:
            logger.log_exception(ex)
            ErrorWindowController(str(ex), self)
        except Exception as e:
            logger.log_exception(e)
            ErrorWindowController("Не удалось удалить заметку", self)


class ErrorWindowController(QtWidgets.QDialog):
    """контроллер окна отображений ошибок"""
    def __init__(self, message: str = None, parent=None):
        try:
            QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Dialog)
            self.parent = parent
            self.message = message
            self.ui = Ui_Exception()
            self.ui.setupUi(self)
            # загрузка изображения (жёлтый треугольник)
            self.ui.image_label.setPixmap(QPixmap("gui/warning.png"))
            self.ui.message_label.setText(message)
            self.setWindowTitle("Exception")
            self.show()
        except Exception as e:
            logger.log_exception(e)


class CalendarWindowController(QtWidgets.QDialog):
    """контроллер окна изменения даты"""
    def __init__(self, cur: MyDate, parent: NoteEditorController=None):
        try:
            # создаём диалоговое окно
            QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Dialog)
            self.parent = parent
            self.ui = Ui_CalendarDialog()
            self.ui.setupUi(self)
            # связываем выбор даты с кнопкой на календаре
            self.ui.calendarWidget.setSelectedDate(QDate(cur.get_year(), cur.get_month_number(), cur.get_day()))
            self.ui.ok_button.clicked.connect(self.change_date)
            self.show()
        except Exception as e:
            logger.log_exception(e)
            ErrorWindowController("Не удалось открыть окно выбора даты!", self)

    def change_date(self):
        """обработка нажатия на кнопку ОК"""
        self.parent.date = MyDate(self.ui.calendarWidget.selectedDate())
        self.hide()
