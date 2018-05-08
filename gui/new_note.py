# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newNote.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewTaskForm(object):
    def setupUi(self, NewTaskForm):
        NewTaskForm.setObjectName("NewTaskForm")
        NewTaskForm.resize(315, 278)
        NewTaskForm.setMinimumSize(QtCore.QSize(315, 278))
        NewTaskForm.setMaximumSize(QtCore.QSize(315, 278))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        NewTaskForm.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        NewTaskForm.setFont(font)
        self.start_time_label = QtWidgets.QLabel(NewTaskForm)
        self.start_time_label.setGeometry(QtCore.QRect(230, 10, 47, 13))
        self.start_time_label.setObjectName("start_time_label")
        self.end_time_label = QtWidgets.QLabel(NewTaskForm)
        self.end_time_label.setGeometry(QtCore.QRect(230, 60, 61, 16))
        self.end_time_label.setObjectName("end_time_label")
        self.start_spinner = QtWidgets.QTimeEdit(NewTaskForm)
        self.start_spinner.setGeometry(QtCore.QRect(230, 30, 81, 22))
        self.start_spinner.setObjectName("start_spinner")
        self.end_spinner = QtWidgets.QTimeEdit(NewTaskForm)
        self.end_spinner.setGeometry(QtCore.QRect(230, 80, 81, 22))
        self.end_spinner.setObjectName("end_spinner")
        self.title_line_edit = QtWidgets.QLineEdit(NewTaskForm)
        self.title_line_edit.setGeometry(QtCore.QRect(10, 10, 211, 20))
        self.title_line_edit.setObjectName("title_line_edit")
        self.description_text_panel = QtWidgets.QPlainTextEdit(NewTaskForm)
        self.description_text_panel.setGeometry(QtCore.QRect(10, 40, 211, 231))
        self.description_text_panel.setObjectName("description_text_panel")
        self.add_note_button = QtWidgets.QPushButton(NewTaskForm)
        self.add_note_button.setGeometry(QtCore.QRect(230, 230, 81, 41))
        self.add_note_button.setObjectName("add_note_button")

        self.retranslateUi(NewTaskForm)
        QtCore.QMetaObject.connectSlotsByName(NewTaskForm)

    def retranslateUi(self, NewTaskForm):
        _translate = QtCore.QCoreApplication.translate
        NewTaskForm.setWindowTitle(_translate("NewTaskForm", "Добавление задачи"))
        self.start_time_label.setText(_translate("NewTaskForm", "Начало"))
        self.end_time_label.setText(_translate("NewTaskForm", "Окончание"))
        self.add_note_button.setText(_translate("NewTaskForm", "Добавить\n"
"заметку"))

