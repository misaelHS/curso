# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ejemplo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Ejemplo(object):
    def setupUi(self, Ejemplo):
        if not Ejemplo.objectName():
            Ejemplo.setObjectName(u"Ejemplo")
        Ejemplo.resize(557, 162)
        self.nombreLE = QLineEdit(Ejemplo)
        self.nombreLE.setObjectName(u"nombreLE")
        self.nombreLE.setGeometry(QRect(71, 9, 171, 20))
        self.correoLE = QLineEdit(Ejemplo)
        self.correoLE.setObjectName(u"correoLE")
        self.correoLE.setGeometry(QRect(70, 40, 171, 20))
        self.contrasenaLE = QLineEdit(Ejemplo)
        self.contrasenaLE.setObjectName(u"contrasenaLE")
        self.contrasenaLE.setGeometry(QRect(70, 70, 101, 20))
        self.nombreL = QLabel(Ejemplo)
        self.nombreL.setObjectName(u"nombreL")
        self.nombreL.setGeometry(QRect(9, 9, 37, 16))
        self.correoL = QLabel(Ejemplo)
        self.correoL.setObjectName(u"correoL")
        self.correoL.setGeometry(QRect(10, 40, 33, 16))
        self.contrasenaL = QLabel(Ejemplo)
        self.contrasenaL.setObjectName(u"contrasenaL")
        self.contrasenaL.setGeometry(QRect(10, 70, 56, 16))
        self.enviarPB = QPushButton(Ejemplo)
        self.enviarPB.setObjectName(u"enviarPB")
        self.enviarPB.setGeometry(QRect(70, 100, 61, 23))
        self.mostrarE = QTextEdit(Ejemplo)
        self.mostrarE.setObjectName(u"mostrarE")
        self.mostrarE.setGeometry(QRect(250, 10, 301, 111))
        self.mostarPB = QPushButton(Ejemplo)
        self.mostarPB.setObjectName(u"mostarPB")
        self.mostarPB.setGeometry(QRect(250, 130, 75, 23))
        self.editarPB = QPushButton(Ejemplo)
        self.editarPB.setObjectName(u"editarPB")
        self.editarPB.setGeometry(QRect(180, 100, 61, 23))
        self.mostrarB = QPushButton(Ejemplo)
        self.mostrarB.setObjectName(u"mostrarB")
        self.mostrarB.setGeometry(QRect(180, 70, 61, 23))

        self.retranslateUi(Ejemplo)

        QMetaObject.connectSlotsByName(Ejemplo)
    # setupUi

    def retranslateUi(self, Ejemplo):
        Ejemplo.setWindowTitle(QCoreApplication.translate("Ejemplo", u"Form", None))
        self.nombreL.setText(QCoreApplication.translate("Ejemplo", u"Nombre", None))
        self.correoL.setText(QCoreApplication.translate("Ejemplo", u"Correo", None))
        self.contrasenaL.setText(QCoreApplication.translate("Ejemplo", u"Contrasena", None))
        self.enviarPB.setText(QCoreApplication.translate("Ejemplo", u"Enviar", None))
        self.mostarPB.setText(QCoreApplication.translate("Ejemplo", u"Mostrar datos", None))
        self.editarPB.setText(QCoreApplication.translate("Ejemplo", u"Editar", None))
        self.mostrarB.setText(QCoreApplication.translate("Ejemplo", u"Mostrar", None))
    # retranslateUi

