import sys   # В модуле sys содержатся функции и константы для взаимодействия с интерпретатором Python.
import traceback   # Модуль traceback предоставляет стандартный интерфейс для извлечения, форматирования и печати трассировок стека программ Python

'''Обеспечивается связь с содержимым указанных файлов, находящихся в соответствующих папках'''
from main import MyWin
from utility.my_date import *
from gui.new_note import *

# QtGui содержит классы для интеграции систем окон, обработки событий,
# 2D-графики, базовой обработки изображений, шрифтов и текста.
# Модуль QtWidgets содержит классы,
# которые обеспечивают набор UI-элементов для создания классических пользовательских интерфейсов.
from PyQt5 import QtCore, QtGui, QtWidgets

'''Обеспечивается связь с содержимым указанных файлов, находящихся в соответствующих папках'''
from utility.my_time import MyTime
from utility.note import Note
from utility.note_comparator import NoteComparator
from utility.note_loader import NoteLoader


class NewNoteController(QtWidgets.QDialog):
    ''''''
    def __init__(self, date=None, parent: MyWin = None):
        ''''''
        try:
            QtWidgets.QWidget.__init__(self, parent)
            self.parent = parent
            self.date = date
            self.ui = Ui_NewTaskForm()
            self.ui.setupUi(self)
            self.ui.add_note_button.clicked.connect(self.add_note_btn_click)
            self.withoutTime = False
        except Exception as e:
            print("NewNoteController __init__ exception", e)

    def add_note_btn_click(self):
        ''''''
        try:
            note = Note(MyTime(s=self.ui.start_spinner.text()),
                        MyTime(s=self.ui.end_spinner.text()),
                        MyDate(date=self.date),
                        self.ui.title_line_edit.text(),
                        self.ui.description_text_panel.toPlainText(),
                        )
            try:
                NoteComparator.compare_note_with_array(note, self.parent.selected_week_notes[MyDate(self.date).get_number_of_day()])
                self.parent.selected_week_notes[MyDate(self.date).get_number_of_day()].append(note)
                cell_row, cell_column = self.get_row_col(note.get_start(), MyDate(self.date))
                cell_row_end, cell_column_end = self.get_row_col(note.get_end(), MyDate(self.date))
                while cell_row < cell_row_end:
                    item = QtWidgets.QTableWidgetItem()
                    brush = QtGui.QBrush(QtGui.QColor(19, 255, 74))
                    brush.setStyle(QtCore.Qt.Dense4Pattern)
                    item.setBackground(brush)
                    self.parent.ui.tableWidget.setItem(cell_row, cell_column, item)
                    cell_row += 1

                self.parent.ui.listWidget.addItem(str(note))
                NoteLoader().upload(note)
            except Exception as e:
                print(e)
                for i in traceback.format_exception(*sys.exc_info()):
                    print(i)

        except Exception as e:
            print(e)
            for i in traceback.format_exception(*sys.exc_info()):
                print(i)
            print(traceback.format_exception(*sys.exc_info()))

    def set_date(self, date):
        self.date = date

    """
        возврат строки таблицы, в зависимости от времени
        время передается в качечтве строки line
    """
    @staticmethod
    def get_row_col(time: MyTime, date: MyDate):
        ''''''
        hours = time.hour()
        minutes = time.minute()
        cell_row = int(hours) * 4 + int(minutes) // 15
        cell_column = date.get_number_of_day()
        return cell_row, cell_column
