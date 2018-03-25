# Python 3. PyQt4
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore


# Графика
class Window_os(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(600, 600)
        self.setWindowTitle('Зап модуля')  # Заголовок

        # БЛОК РАЗМЕТКИ
        grid = QtGui.QGridLayout()  # создание сетки
        self.lbl_1 = QtGui.QLabel('<font color="red"> <H2>Текст основной' +
                                  ' программы</H2><font>')
        grid.addWidget(self.lbl_1, 0, 0)
        # self.setStyleSheet("QFrame {background-color: #2e6979;}")
        # --- ---

        viewport = Mod(self)  # импорт модуля
        viewport.setStyleSheet("background-color: #517852; text-align: justify")
        grid.addWidget(viewport, 1, 0)
        # --- ---
        frame_1 = QtGui.QFrame()
        frame_1.setFrameShape(0)  # 0 - отключить рамку
        frame_1_lay = QtGui.QGridLayout(frame_1)
        grid.addWidget(frame_1, 2, 0)  # Фрейм 1
        # ---
        self.pole = QtGui.QTextEdit('<H2>Поле основной программы<H2>')
        frame_1_lay.addWidget(self.pole, 0, 0)
        # --- ---
        self.btn = QtGui.QPushButton('Вставить')
        frame_1_lay.addWidget(self.btn, 1, 0)
        # --- ---
        self.setLayout(grid)  # установка менеджера компоновки


class Mod(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # БЛОК РАЗМЕТКИ
        hbox = QtGui.QHBoxLayout()  # создание сетки
        pole1 = QtGui.QTextEdit()
        hbox.addWidget(pole1)
        # ---
        pole2 = QtGui.QTextEdit()
        hbox.addWidget(pole2)
        # --- ---
        self.setLayout(hbox)  # установка менеджера компоновки


# КОНЕЦ
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Window_os()  # создаёт экземпляр окна из класса
    window.show()  # запускает окно
    sys.exit(app.exec_())