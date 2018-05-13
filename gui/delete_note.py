# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_note.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeleteNote(object):
    def setupUi(self, DeleteNote):
        DeleteNote.setObjectName("DeleteNote")
        DeleteNote.resize(300, 93)
        self.label = QtWidgets.QLabel(DeleteNote)
        self.label.setGeometry(QtCore.QRect(10, 0, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.ok_button = QtWidgets.QPushButton(DeleteNote)
        self.ok_button.setGeometry(QtCore.QRect(210, 60, 75, 23))
        self.ok_button.setObjectName("ok_button")

        self.retranslateUi(DeleteNote)
        QtCore.QMetaObject.connectSlotsByName(DeleteNote)

    def retranslateUi(self, DeleteNote):
        _translate = QtCore.QCoreApplication.translate
        DeleteNote.setWindowTitle(_translate("DeleteNote", "Вы уверены?"))
        self.label.setText(_translate("DeleteNote", "Вы уверены?\n"
"Нажмите \"ОК\" чтобы удалить заметку навсегда"))
        self.ok_button.setText(_translate("DeleteNote", "ОК"))

