import json   # Модуль json выполняет всю работу по преобразованию данных из формата Json в значения Python и обратно.
import sys   # В модуле sys содержатся функции и константы для взаимодействия с интерпретатором Python.
import traceback   # Модуль traceback предоставляет стандартный интерфейс для извлечения, форматирования и печати трассировок стека программ Python

from controllers.new_note import *
from utility.my_date import *
from gui.gui import *
# Модуль QtCore содержит ядро с неграфической функциональностью.
# Этот модуль используется для работы с временем, файлами, папками,
# различными типами файлов, потоками, адресами URL, MIME-типами и процессами.

# QtGui содержит классы для интеграции систем окон, обработки событий,
# 2D-графики, базовой обработки изображений, шрифтов и текста.
from PyQt5 import QtCore, QtGui, QtWidgets
# Модуль QtWidgets содержит классы,
# которые обеспечивают набор UI-элементов для создания классических пользовательских интерфейсов.
# Виджет Qwidget является базовым классом для всех объектов интерфейса пользователя в PyQt5.
# QcheckBox – это виджет, который имеет два состояния: вкл. И выкл. Это квадратик с меткой.
# Как правило, чекбоксы используют, чтобы представить функции приложения, которые могут быть включены или выключены.
# Qapplication – приложение, с которого начинается построение интерфейса.
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt

'''Обеспечивается связь с содержимым указанных файлов, находящихся в соответствующих папках'''
from utility.my_time import MyTime
from utility.note import Note
from utility.note_comparator import NoteComparator
from utility.note_loader import NoteLoader


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        try:
            QtWidgets.QWidget.__init__(self, parent)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.selected_week_notes = None
            self.ui.openNewNoteButton.clicked.connect(self.open_new_note_window)
            self.new_note_window = NewNoteController(parent=self)
            self.ui.listWidget.itemClicked.connect(self.fun)
            self.ui.calendarWidget.selectionChanged.connect(self.selected_date)
            self.ui.tableWidget.pressed.connect(self.selected_item)
            self.current_selected_date = MyDate()
            self.current_selected_date.set_qt_date(self.ui.calendarWidget.selectedDate())
            #self.selected_week_notes = NoteLoader().load_notes_by_week_number(self.current_selected_date)
            self.load_current_week_notes(self.current_selected_date)
            self.load_current_day_notes(self.current_selected_date)
            self.last_selected_date = None

        except Exception as e:
            print(e)
            for i in traceback.format_exception(*sys.exc_info()):
                print(i)

    def selected_date(self):
        self.last_selected_date = self.current_selected_date
        self.current_selected_date = MyDate()
        self.current_selected_date.set_qt_date(self.ui.calendarWidget.selectedDate())
        cur = self.current_selected_date
        last = self.last_selected_date
        if cur.get_number_of_week() != last.get_number_of_week() or cur.get_year() != last.get_year():
            for i in range(7):
                self.selected_week_notes[i].clear()
            self.clean_table()
            self.load_current_week_notes(cur)

        if cur != last:
            self.load_current_day_notes(cur)

    def open_new_note_window(self):
        self.new_note_window.set_date(self.ui.calendarWidget.selectedDate())
        self.new_note_window.show()

    def fun(self, item):
        print(item.text())

    def selected_item(self, model_index):
        hours_start = model_index.row() * 15 // 60
        minutes_start = model_index.row() * 15 % 60
        time = MyTime(h=hours_start, m=minutes_start)
        day = day_array[model_index.column()]
        selected = '(' + str(time) + ' ; ' + day + ')'
        print(selected)

    """
        очистка таблицы от задач
        используется при изменении номера недели выбранной даты
    """
    def clean_table(self):
        for cell_row in range(96):
            for cell_column in range(7):
                item = QtWidgets.QTableWidgetItem()
                brush = QtGui.QBrush(QtGui.QColor(255,255,255))
                item.setBackground(brush)
                self.ui.tableWidget.setItem(cell_row, cell_column, item)

    def load_current_week_notes(self, cur: MyDate):
        self.selected_week_notes = NoteLoader().load_notes_by_week_number(selected_date=cur)
        for array in self.selected_week_notes:
            for note in array:
                cell_row, cell_column = NewNoteController.get_row_col(note.get_start(), note.get_date())
                cell_row_end, cell_column_end = NewNoteController.get_row_col(note.get_end(), note.get_date())
                while cell_row < cell_row_end:
                    item = QtWidgets.QTableWidgetItem()
                    brush = QtGui.QBrush(QtGui.QColor(19, 255, 74))
                    brush.setStyle(QtCore.Qt.Dense4Pattern)
                    item.setBackground(brush)
                    self.ui.tableWidget.setItem(cell_row, cell_column, item)
                    cell_row += 1

    def load_current_day_notes(self, cur: MyDate):
        notes = self.selected_week_notes[cur.get_number_of_day()]
        self.ui.listWidget.clear()
        for i in notes:
            self.ui.listWidget.addItem(str(i))


if __name__ == "__main__":
    d = MyDate()
    d.set_date(day=1, month=1, year=2018)
    NoteLoader().load_notes_by_week_number(d)
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())



