import sys
from gui.gui import *
from gui.newNote import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt

str_select_date = ''

class NewNoteParams(object):
    def __init__(self, startTime, endTime, title, description):
        self.startTime = startTime
        self.endTime = endTime
        self.title = title
        self.description = description


class NewNoteController(QtWidgets.QDialog):
    def __init__(self,date = None, parent=None):
        try:
            QtWidgets.QWidget.__init__(self, parent)
            self.parent = parent
            self.date = date
            self.ui = Ui_NewTaskForm()
            self.ui.setupUi(self)
            self.ImportantButtom()
            self.setupWithoutTimeCheckBox()
            self.ui.addNoteButton.clicked.connect(self.addNoteButtonClick)
            self.withoutTime = False

        except:
            print("NewNoteController __init__ exception")

    def setupWithoutTimeCheckBox(self):
        self.ui.checkBoxWithoutTime.setGeometry(QtCore.QRect(230, 120, 81, 17))
        self.ui.checkBoxWithoutTime.setObjectName("checkBoxWithoutTime")
        self.ui.checkBoxWithoutTime.toggle()
        self.ui.checkBoxWithoutTime.stateChanged.connect(self.withoutTime)
        _translate = QtCore.QCoreApplication.translate
        self.ui.checkBoxWithoutTime.setText(_translate("NewTaskForm", "Без времени"))


    def addNoteButtonClick(self):
        try:
            str_item = ''
            st = self.ui.checkBoxWithoutTime.checkState()
            print(st == Qt.Checked)
            self.withoutTime = (st == Qt.Checked)
            if not self.withoutTime:
                str_item += str(self.ui.startTimeSpinner.text())
                str_item += '\n' + str(self.ui.endTimeEdit.text()) + '\n'
            str_item += str(self.date.toString()) + '\n'
            str_item += str(self.ui.nameTextPanel.text()) + '\n'
            str_item += str(self.ui.descriptionTextPanel.toPlainText())
           # self.ui.checkBoxWithoutTime(QWebSettings.StandardFont, 'Times New Roman')  #Попытка изменить шрифт
            self.parent.ui.listWidget.addItem(str_item)
                                                                              # Куча попыток связать кнопку "важно" с изменением шрифта

            self.withoutTime = False
        except:
            print("111111111111111111111111111")

    def setDate(self, date):
        self.date = date

    def withoutTime(self, state):
        self.withoutTime = (state == Qt.Checked)
        print("w ", self.withoutTime)
''' def 
'''

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        try:
            QtWidgets.QWidget.__init__(self, parent)
            self.ui = Ui_MainWindow()
            #self.
            self.ui.setupUi(self)
            self.ui.openNewNoteButton.clicked.connect(self.open_new_note_window)
            self.new_note_params = None
            self.new_note_window = NewNoteController(parent=self)
            #model = QStandardItemModel(lst)
            self.ui.listWidget.itemClicked.connect(self.fun)
            self.ui.calendarWidget.selectionChanged.connect(self.selectedDate)

        except:
            print("error2")

    def selectedDate(self):
        self.ui.label.setText(self.ui.calendarWidget.selectedDate().toString())

    def open_new_note_window(self):
        self.new_note_window.setDate(self.ui.calendarWidget.selectedDate())
        self.new_note_window.show()

    def fun(self, item):
        print(item.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())