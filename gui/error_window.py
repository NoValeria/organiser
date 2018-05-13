# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Exception(object):
    def setupUi(self, Exception):
        Exception.setObjectName("Exception")
        Exception.setWindowModality(QtCore.Qt.WindowModal)
        Exception.resize(320, 128)
        Exception.setMinimumSize(QtCore.QSize(320, 128))
        Exception.setMaximumSize(QtCore.QSize(320, 128))
        Exception.setSizeGripEnabled(False)
        Exception.setModal(False)
        self.message_label = QtWidgets.QLabel(Exception)
        self.message_label.setGeometry(QtCore.QRect(115, 10, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.message_label.setFont(font)
        self.message_label.setWordWrap(True)
        self.message_label.setObjectName("message_label")
        self.image_label = QtWidgets.QLabel(Exception)
        self.image_label.setGeometry(QtCore.QRect(5, 14, 100, 100))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")

        self.retranslateUi(Exception)
        QtCore.QMetaObject.connectSlotsByName(Exception)

    def retranslateUi(self, Exception):
        _translate = QtCore.QCoreApplication.translate
        Exception.setWindowTitle(_translate("Exception", "Dialog"))
        self.message_label.setText(_translate("Exception", "TextLabel"))

