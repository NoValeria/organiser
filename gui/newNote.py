# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newNote.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 320)
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
        Form.setPalette(palette)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 251, 191))
        self.calendarWidget.setObjectName("calendarWidget")
        self.StartTimeLabel = QtWidgets.QLabel(Form)
        self.StartTimeLabel.setGeometry(QtCore.QRect(10, 210, 47, 13))
        self.StartTimeLabel.setObjectName("StartTimeLabel")
        self.EndTimeLabel = QtWidgets.QLabel(Form)
        self.EndTimeLabel.setGeometry(QtCore.QRect(10, 260, 61, 16))
        self.EndTimeLabel.setObjectName("EndTimeLabel")
        self.startTimeSpinner = QtWidgets.QTimeEdit(Form)
        self.startTimeSpinner.setGeometry(QtCore.QRect(10, 230, 118, 22))
        self.startTimeSpinner.setObjectName("startTimeSpinner")
        self.endTimeEdit = QtWidgets.QTimeEdit(Form)
        self.endTimeEdit.setGeometry(QtCore.QRect(10, 280, 118, 22))
        self.endTimeEdit.setObjectName("endTimeEdit")
        self.nameTextPanel = QtWidgets.QLineEdit(Form)
        self.nameTextPanel.setGeometry(QtCore.QRect(332, 10, 131, 20))
        self.nameTextPanel.setObjectName("nameTextPanel")
        self.descriptionTextPanel = QtWidgets.QPlainTextEdit(Form)
        self.descriptionTextPanel.setGeometry(QtCore.QRect(260, 60, 211, 221))
        self.descriptionTextPanel.setObjectName("descriptionTextPanel")
        self.addNoteButton = QtWidgets.QPushButton(Form)
        self.addNoteButton.setGeometry(QtCore.QRect(344, 290, 111, 23))
        self.addNoteButton.setObjectName("addNoteButton")
        self.titleLabel = QtWidgets.QLabel(Form)
        self.titleLabel.setGeometry(QtCore.QRect(270, 13, 47, 13))
        self.titleLabel.setObjectName("titleLabel")
        self.descriptionLabel = QtWidgets.QLabel(Form)
        self.descriptionLabel.setGeometry(QtCore.QRect(260, 40, 61, 16))
        self.descriptionLabel.setObjectName("descriptionLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.StartTimeLabel.setText(_translate("Form", "Начало"))
        self.EndTimeLabel.setText(_translate("Form", "Окончание"))
        self.addNoteButton.setText(_translate("Form", "Добавить заметку"))
        self.titleLabel.setText(_translate("Form", "Название"))
        self.descriptionLabel.setText(_translate("Form", "Описание:"))

