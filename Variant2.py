import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QGridLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QApplication, QMessageBox, QMainWindow)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize, Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)


        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Organiser')
        self.show()

        # Наследуемся от QMainWindow

        grid_layout = QGridLayout()

        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(3)
        table.setRowCount(1)  # и одну строку в таблице

        table.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3"])

        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)

        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)


    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    
    sys.exit(app.exec())

