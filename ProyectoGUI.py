#************************** Funciones para trabajar con Qtcretor
import sys
#from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow, QLineEdit, QApplication, QMessageBox, QFileDialog
#from Ejemplo import Ui_Ejemplo
from estudiante import Estudiante
from Proyecto import *
from cliente import cliente
import socket
import pickle
#**************************** Funciones
from package.modulo6 import *
import re

class ProyectoGUI(QMainWindow):

    def __init__(self):
        super(ProyectoGUI,self).__init__()
        self.ui=Ui_Proyecto() #del archivo *.ui
        self.ui.setupUi(self)

        self.ui.conectarPB.setDisabled(True)
        self.ui.enviarDatoPB.setDisabled(True)
        self.ui.enviarArchiPB.setDisabled(True)
        self.ui.mostrarPB.setDisabled(True)
        self.ui.archivoG.setDisabled(True)

       # enviarDatoPB v
       # enviarArchiPB v
       # mostrarPB
       # buscarPB v
       # conectarPB v

       # estudianteG
       # archivoG v
       # conexionG

       # nombreL
       # correoL
       # contraL
       # ipL
       # puertoL

       # nombreLE v
       # correoLE v
       # contraLE v
       # ipLE v
       # puertoLE v
       # archivoLE

        self.ui.ipLE.textChanged.connect(self.activarConectarB)
        self.ui.puertoLE.textChanged.connect(self.activarConectarB)
        self.ui.conectarPB.clicked.connect(self.conectar)

        self.ui.enviarDatoPB.clicked.connect(self.enviarEstudiante)
        self.ui.enviarArchiPB.clicked.connect(self.enviarArchivo)
        self.ui.buscarPB.clicked.connect(self.buscarArchivo)
        self.ui.mostrarPB.clicked.connect(self.mostrarContrasena)

        self.ui.nombreLE.textEdited.connect(self.activarEnviarEstudianteB)
        self.ui.correoLE.textEdited.connect(self.activarEnviarEstudianteB)
        self.ui.contraLE.textEdited.connect(self.activarEnviarEstudianteB)

#---------------------
        self.ui.ipLE.setText('3.16.226.150')
        #self.ui.ipLE.setText('localhost')
        self.ui.puertoLE.setText('9998')

    def activarConectarB(self):
        if self.ui.ipLE.text() and self.ui.puertoLE.text():
            self.ui.conectarPB.setEnabled(True)
        else:
            self.ui.conectarPB.setDisabled(True)

    def conectar(self):
        if self.ui.conectarPB.text() == '3.16.226.150':
            ip = self.ui.ipLE.text()
            puerto = int(self.ui.puertoLE.text())

            self.cliente = cliente(ip, puerto)
            self.cliente.conectar()

            self.ui.conectarPB.setText('Desconectar')

            self.ui.estudianteG.setDisabled(True)

        elif self.ui.conectarPB.text() == 'Desconectar':
            self.cliente.desconectar()

            self.ui.conectarPB.setText('Conectar')

            self.ui.estudianteG.setDisabled(True)
            self.ui.archivoG.setDisabled(True)

    def activarEnviarEstudianteB(self):
        if self.ui.nombreLE.text() and self.ui.correoLE.text() and self.ui.contraLE.text():
            self.ui.enviarDatoPB.setEnabled(True)
            self.ui.mostrarPB.setEnabled(True)
        else:
            self.ui.enviarDatoPB.setDisabled(True)

    def mostrarContrasena(self):
        if self.ui.contraLE.echoMode()==QLineEdit.Password:
            self.ui.contraLE.setEchoMode(QLineEdit.Normal)
            self.ui.mostrarPB.setText('Ocultar')
        else:
            self.ui.contraLE.setEchoMode(QLineEdit.Password)
            self.ui.mostrarPB.setText('Mostrar')

    def enviarEstudiante(self):
        e = Estudiante(
            self.ui.nombreLE.text(),
            self.ui.correoLE.text(),
            self.ui.contraLE.text()
        )

        self.ui.archivoG.setEnabled(True)

#        res = self.cliente.enviar(e)
#        self.mostrarDialog(res)

    def buscarArchivo(self):
        filename, _ = QFileDialog.getOpenFileName(filter='*.zip')
        self.ui.archivoLE.setText(filename)
        self.ui.enviarArchiPB.setDisabled(False)

    def activarEnviarArchivoB(self):
        if self.ui.archivoLE.text():
            self.ui.enviarArchiPB.setEnabled(True)
        else:
            self.ui.enviarArchiPB.setDisabled(True)

    def enviarArchivo(self):
        filename = self.ui.archivoLE.text()
        file = open(filename, 'rb')  # para hacer pruebas se puede poner el archivo 'test.zip' en lugar de filename

    #    res = self.cliente.enviar(file.read())
    #    self.mostrarDialog(res)

    def mostrarDialog(self, msj):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Information)
        dialog.setText(msj)
        dialog.setWindowTitle('Mensaje recibido')
        dialog.setStandardButtons(QMessageBox.Ok)
        dialog.exec_()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = ProyectoGUI()
    window.show()
    sys.exit(app.exec_())


