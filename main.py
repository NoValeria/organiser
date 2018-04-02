import sys
from gui.gui import *
from gui.calendar import *
from gui.newNote import *
from PyQt5 import QtCore, QtGui, QtWidgets

str_select_date = ''

class NewNoteController(QtWidgets.QDialog):
    def __init__(self, parent=None):
        try:
            QtWidgets.QWidget.__init__(self, parent)
            self.parent = parent
            self.ui = Ui_Form()
            self.ui.setupUi(self)
        except:
            pass


class Calendar(QtWidgets.QDialog):
    def __init__(self, parent=None):
        try:
            QtWidgets.QWidget.__init__(self, parent)
            self.parent = parent
            self.ui = Ui_Dialog_Calendar()
            self.ui.setupUi(self)
            self.ui.ok_button.clicked.connect(self.fun)
        except:
            print("error")

    def fun(self):
        global str_select_date
        str_select_date = self.ui.calendarWidget.selectedDate().toString()
        print(str_select_date)
        self.parent.ui.label.setText(str_select_date)
        self.hide()


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        try:
            QtWidgets.QWidget.__init__(self, parent)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.MyFunction)
            self.ui.openNewNoteButton.clicked.connect(self.open_new_note_window)
            self.new_note_window = NewNoteController(parent=self)
            self.calendar = Calendar(parent=self)
        except:
            print("error2")

    def open_new_note_window(self):
        self.new_note_window.show()

    def MyFunction(self):
        self.calendar.show()
        """if self.ui.pushButton_2.isHidden():
            self.ui.pushButton_2.show()
        else:
            self.ui.pushButton_2.hide()"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())