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
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(10, 230, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(Form)
        self.timeEdit_2.setGeometry(QtCore.QRect(10, 280, 118, 22))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(260, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(260, 70, 211, 241))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.StartTimeLabel.setText(_translate("Form", "Начало"))
        self.EndTimeLabel.setText(_translate("Form", "Окончание"))

