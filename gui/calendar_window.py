# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CalendarDialog(object):
    def setupUi(self, CalendarDialog):
        CalendarDialog.setObjectName("CalendarDialog")
        CalendarDialog.setWindowModality(QtCore.Qt.WindowModal)
        CalendarDialog.resize(320, 225)
        CalendarDialog.setMinimumSize(QtCore.QSize(320, 225))
        CalendarDialog.setMaximumSize(QtCore.QSize(320, 225))
        CalendarDialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        CalendarDialog.setModal(True)
        self.calendarWidget = QtWidgets.QCalendarWidget(CalendarDialog)
        self.calendarWidget.setGeometry(QtCore.QRect(4, 10, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.ok_button = QtWidgets.QPushButton(CalendarDialog)
        self.ok_button.setGeometry(QtCore.QRect(240, 200, 75, 23))
        self.ok_button.setObjectName("ok_button")

        self.retranslateUi(CalendarDialog)
        QtCore.QMetaObject.connectSlotsByName(CalendarDialog)

    def retranslateUi(self, CalendarDialog):
        _translate = QtCore.QCoreApplication.translate
        CalendarDialog.setWindowTitle(_translate("CalendarDialog", "Выберите дату"))
        self.ok_button.setText(_translate("CalendarDialog", "ОК"))

