# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaSalir.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/salir/img/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color:rgb(135, 154, 209)")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 230, 191, 32))
        self.buttonBox.setStyleSheet("background-color:#FEFBE7;font-weight: bold;")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 160, 221, 31))
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.labelImagen = QtWidgets.QLabel(Dialog)
        self.labelImagen.setGeometry(QtCore.QRect(150, 30, 121, 111))
        self.labelImagen.setText("")
        self.labelImagen.setPixmap(QtGui.QPixmap(":/salir/img/salirt.png"))
        self.labelImagen.setScaledContents(True)
        self.labelImagen.setObjectName("labelImagen")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SALIR"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">¿Seguro que desea salir?</span></p></body></html>"))
import recursos_rc