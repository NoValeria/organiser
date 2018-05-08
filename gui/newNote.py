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
        self.StartTimeLabel = QtWidgets.QLabel(NewTaskForm)
        self.StartTimeLabel.setGeometry(QtCore.QRect(230, 10, 47, 13))
        self.StartTimeLabel.setObjectName("StartTimeLabel")
        self.EndTimeLabel = QtWidgets.QLabel(NewTaskForm)
        self.EndTimeLabel.setGeometry(QtCore.QRect(230, 60, 61, 16))
        self.EndTimeLabel.setObjectName("EndTimeLabel")
        self.startTimeSpinner = QtWidgets.QTimeEdit(NewTaskForm)
        self.startTimeSpinner.setGeometry(QtCore.QRect(230, 30, 81, 22))
        self.startTimeSpinner.setObjectName("startTimeSpinner")
        self.endTimeSpinner = QtWidgets.QTimeEdit(NewTaskForm)
        self.endTimeSpinner.setGeometry(QtCore.QRect(230, 80, 81, 22))
        self.endTimeSpinner.setObjectName("endTimeSpinner")
        self.nameTextPanel = QtWidgets.QLineEdit(NewTaskForm)
        self.nameTextPanel.setGeometry(QtCore.QRect(10, 10, 211, 20))
        self.nameTextPanel.setObjectName("nameTextPanel")
        self.descriptionTextPanel = QtWidgets.QPlainTextEdit(NewTaskForm)
        self.descriptionTextPanel.setGeometry(QtCore.QRect(10, 40, 211, 231))
        self.descriptionTextPanel.setObjectName("descriptionTextPanel")
        self.addNoteButton = QtWidgets.QPushButton(NewTaskForm)
        self.addNoteButton.setGeometry(QtCore.QRect(230, 230, 81, 41))
        self.addNoteButton.setObjectName("addNoteButton")
        self.checkBoxWithoutTime = QtWidgets.QCheckBox(NewTaskForm)
        self.checkBoxWithoutTime.setGeometry(QtCore.QRect(230, 120, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.checkBoxWithoutTime.setFont(font)
        self.checkBoxWithoutTime.setObjectName("checkBoxWithoutTime")
        self.checkBoxDone = QtWidgets.QCheckBox(NewTaskForm)
        self.checkBoxDone.setGeometry(QtCore.QRect(230, 150, 81, 17))
        self.checkBoxDone.setObjectName("checkBoxDone")

        self.retranslateUi(NewTaskForm)
        QtCore.QMetaObject.connectSlotsByName(NewTaskForm)

    def retranslateUi(self, NewTaskForm):
        _translate = QtCore.QCoreApplication.translate
        NewTaskForm.setWindowTitle(_translate("NewTaskForm", "Добавление задачи"))
        self.StartTimeLabel.setText(_translate("NewTaskForm", "Начало"))
        self.EndTimeLabel.setText(_translate("NewTaskForm", "Окончание"))
        self.addNoteButton.setText(_translate("NewTaskForm", "Добавить\n"
"заметку"))
        self.checkBoxWithoutTime.setText(_translate("NewTaskForm", "Без времени"))
        self.checkBoxDone.setText(_translate("NewTaskForm", "Выполнено"))

