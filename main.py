import sys
from gui.gui import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.MyFunction)

    def MyFunction(self):
        if self.ui.pushButton_2.isHidden():
            self.ui.pushButton_2.show()
        else:
            self.ui.pushButton_2.hide()

        date = self.ui.calendarWidget.selectedDate()
        self.ui.pushButton.setText(str(date))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())