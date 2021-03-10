# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Proyecto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Proyecto(object):
    def setupUi(self, Proyecto):
        if not Proyecto.objectName():
            Proyecto.setObjectName(u"Proyecto")
        Proyecto.resize(282, 376)
        self.enviarDatoPB = QPushButton(Proyecto)
        self.enviarDatoPB.setObjectName(u"enviarDatoPB")
        self.enviarDatoPB.setGeometry(QRect(10, 240, 261, 23))
        self.enviarArchiPB = QPushButton(Proyecto)
        self.enviarArchiPB.setObjectName(u"enviarArchiPB")
        self.enviarArchiPB.setGeometry(QRect(10, 340, 261, 23))
        self.estudianteG = QGroupBox(Proyecto)
        self.estudianteG.setObjectName(u"estudianteG")
        self.estudianteG.setGeometry(QRect(10, 120, 261, 111))
        self.nombreL = QLabel(self.estudianteG)
        self.nombreL.setObjectName(u"nombreL")
        self.nombreL.setGeometry(QRect(10, 20, 47, 13))
        self.correoL = QLabel(self.estudianteG)
        self.correoL.setObjectName(u"correoL")
        self.correoL.setGeometry(QRect(10, 50, 47, 13))
        self.contraL = QLabel(self.estudianteG)
        self.contraL.setObjectName(u"contraL")
        self.contraL.setGeometry(QRect(10, 80, 61, 16))
        self.nombreLE = QLineEdit(self.estudianteG)
        self.nombreLE.setObjectName(u"nombreLE")
        self.nombreLE.setGeometry(QRect(80, 20, 171, 21))
        self.correoLE = QLineEdit(self.estudianteG)
        self.correoLE.setObjectName(u"correoLE")
        self.correoLE.setGeometry(QRect(80, 50, 171, 21))
        self.contraLE = QLineEdit(self.estudianteG)
        self.contraLE.setObjectName(u"contraLE")
        self.contraLE.setGeometry(QRect(80, 80, 101, 21))
        self.mostrarPB = QPushButton(self.estudianteG)
        self.mostrarPB.setObjectName(u"mostrarPB")
        self.mostrarPB.setGeometry(QRect(190, 80, 61, 23))
        self.archivoG = QGroupBox(Proyecto)
        self.archivoG.setObjectName(u"archivoG")
        self.archivoG.setGeometry(QRect(10, 270, 261, 61))
        self.buscarPB = QPushButton(self.archivoG)
        self.buscarPB.setObjectName(u"buscarPB")
        self.buscarPB.setGeometry(QRect(190, 20, 61, 21))
        self.archivoLE = QLineEdit(self.archivoG)
        self.archivoLE.setObjectName(u"archivoLE")
        self.archivoLE.setGeometry(QRect(10, 20, 161, 21))
        self.conexionG = QGroupBox(Proyecto)
        self.conexionG.setObjectName(u"conexionG")
        self.conexionG.setGeometry(QRect(10, 10, 261, 91))
        self.ipLE = QLineEdit(self.conexionG)
        self.ipLE.setObjectName(u"ipLE")
        self.ipLE.setGeometry(QRect(10, 40, 111, 21))
        self.puertoLE = QLineEdit(self.conexionG)
        self.puertoLE.setObjectName(u"puertoLE")
        self.puertoLE.setGeometry(QRect(140, 40, 113, 21))
        self.ipL = QLabel(self.conexionG)
        self.ipL.setObjectName(u"ipL")
        self.ipL.setGeometry(QRect(10, 20, 47, 13))
        self.puertoL = QLabel(self.conexionG)
        self.puertoL.setObjectName(u"puertoL")
        self.puertoL.setGeometry(QRect(140, 20, 47, 13))
        self.conectarPB = QPushButton(self.conexionG)
        self.conectarPB.setObjectName(u"conectarPB")
        self.conectarPB.setGeometry(QRect(90, 60, 75, 23))

        self.retranslateUi(Proyecto)

        QMetaObject.connectSlotsByName(Proyecto)
    # setupUi

    def retranslateUi(self, Proyecto):
        Proyecto.setWindowTitle(QCoreApplication.translate("Proyecto", u"Form", None))
        self.enviarDatoPB.setText(QCoreApplication.translate("Proyecto", u"Enviar datos", None))
        self.enviarArchiPB.setText(QCoreApplication.translate("Proyecto", u"Enviar archivo", None))
        self.estudianteG.setTitle(QCoreApplication.translate("Proyecto", u"Datos del estudiante", None))
        self.nombreL.setText(QCoreApplication.translate("Proyecto", u"Nombre", None))
        self.correoL.setText(QCoreApplication.translate("Proyecto", u"Correo", None))
        self.contraL.setText(QCoreApplication.translate("Proyecto", u"Contrase\u00f1a", None))
        self.mostrarPB.setText(QCoreApplication.translate("Proyecto", u"Mostrar", None))
        self.archivoG.setTitle(QCoreApplication.translate("Proyecto", u"Archivo a enviar", None))
        self.buscarPB.setText(QCoreApplication.translate("Proyecto", u"Buscar", None))
        self.conexionG.setTitle(QCoreApplication.translate("Proyecto", u"Configuraci\u00f3n del servidor", None))
        self.ipL.setText(QCoreApplication.translate("Proyecto", u"IP", None))
        self.puertoL.setText(QCoreApplication.translate("Proyecto", u"Puerto", None))
        self.conectarPB.setText(QCoreApplication.translate("Proyecto", u"Conectar", None))
    # retranslateUi

