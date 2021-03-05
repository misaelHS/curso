#************************** Funciones para trabajar con Qtcretor
#************************** Funciones para trabajar con Qtcretor
from PySide2.QtWidgets import QApplication
#from PySide2.QtWidgets import QMainWindow, QLineEdit
from Ejemplo import *
import sys
#**************************** Funciones
from package.modulo6 import *
import re

class Ejemplo(QMainWindow):

    def __init__(self):
        super(Ejemplo,self).__init__()
        self.ui=Ui_Ejemplo() #del archivo *.ui
        self.ui.setupUi(self)

        #Boton deactivado de inicio
        self.ui.enviarPB.setEnabled(False)
        self.ui.mostarPB.setEnabled(False)


        self.ui.enviarPB.clicked.connect(self.botonEnviar)
        self.ui.mostarPB.clicked.connect(self.botonMostrar)
        self.ui.editarPB.clicked.connect(self.botonEditar)
        self.ui.nombreLE.textEdited.connect(self.textoEditado)
        self.ui.correoLE.textEdited.connect(self.textoEditado)
        self.ui.contrasenaLE.textEdited.connect(self.textoEditado)
        self.ui.mostrarE.textChanged.connect(self.textoEditado)
        self.ui.mostrarB.clicked.connect(self.mostrarPassword)

        #Slot
    def botonEnviar(self):
        print("Se ha enviado el dato correctamente")

        documento = {"Nombre": self.ui.nombreLE.text(), "Correo": self.ui.correoLE.text(),
                     "Contraseña": self.ui.contrasenaLE.text()}
        coleccion.insert_one(documento)

    def botonMostrar(self):
        self.ui.mostrarE.setReadOnly(True)
        for documento in coleccion.find():
               self.ui.mostrarE.append(documento["Nombre"]+" "+documento["Correo"]+" "+documento["Contraseña"])

    def textoEditado(self):


        if (len(self.ui.nombreLE.text())!=0 and len(self.ui.correoLE.text())!=0 and len(self.ui.contrasenaLE.text())!=0):

            correoElectronico = self.ui.correoLE.text()
            correoValidado = validaCorreo(correoElectronico)

            nombreIngresado = self.ui.nombreLE.text()
            nombreValidado = validaNombre(nombreIngresado)

            self.ui.contrasenaLE.setEchoMode(QLineEdit.Password)
            passwordIngresado = self.ui.contrasenaLE.text()
            passwordValidado = validaPassword(passwordIngresado)

            if (nombreValidado==True):
                print("Nombre corecto")

                if (correoValidado==True):
                    print("Correo corecto")

                    if (passwordValidado == True):
                        print("Password corecto")

                        self.ui.enviarPB.setEnabled(True)
                        self.ui.mostarPB.setEnabled(True)

                    else:
                         print("Pasword incorecto")

                else:
                    print("Correo incorecto")

            else:
                print("Nombre incorecto")


    def botonEditar(self):
        if (len(self.ui.nombreLE.text())!=0 and len(self.ui.correoLE.text())!=0 and len(self.ui.contrasenaLE.text())!=0):
            documento = {"Nombre": self.ui.nombreLE.text(), "Correo": self.ui.correoLE.text(),
                         "Contraseña": self.ui.contrasenaLE.text()}
            coleccion.insert_one(documento)

    def mostrarPassword(self):
        if self.ui.contrasenaLE.echoMode()==QLineEdit.Password:
            self.ui.contrasenaLE.setEchoMode(QLineEdit.Normal)
            self.ui.mostrarB.setText('Ocultar')
        else:
            self.ui.contrasenaLE.setEchoMode(QLineEdit.Password)
            self.ui.mostrarB.setText('Mostrar')



if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Ejemplo()
    window.show()
    sys.exit(app.exec_())

