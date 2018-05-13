# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deadline.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Deadline(object):
    def setupUi(self, Deadline):
        Deadline.setObjectName("Deadline")
        Deadline.setWindowModality(QtCore.Qt.WindowModal)
        Deadline.resize(300, 400)
        Deadline.setMinimumSize(QtCore.QSize(300, 400))
        Deadline.setMaximumSize(QtCore.QSize(300, 400))
        self.listWidget = QtWidgets.QListWidget(Deadline)
        self.listWidget.setGeometry(QtCore.QRect(20, 20, 256, 361))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Deadline)
        QtCore.QMetaObject.connectSlotsByName(Deadline)

    def retranslateUi(self, Deadline):
        _translate = QtCore.QCoreApplication.translate
        Deadline.setWindowTitle(_translate("Deadline", "Ближайшие задачи"))

