# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_Calendar(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(247, 215)
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 248, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setGeometry(QtCore.QRect(80, 190, 75, 23))
        self.ok_button.setObjectName("ok_button")
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(170, 190, 75, 23))
        self.cancel_button.setObjectName("cancel_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ok_button.setText(_translate("Dialog", "OK"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))

