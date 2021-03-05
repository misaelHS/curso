
from tkinter import *       #librerias para interfaz grafica
from tkinter import ttk
from tkinter import messagebox
import pymongo                      #libreria para hacer la gestion de base de datos
from bson.objectid import ObjectId  #libreria para hacer la conversion hacia un objeto ID

mongoHost="localhost"               #se configuran los parametros para la conexion a la BD
mongoPuerto="27017"
mongoTimeout="1000"
mongoURL = "mongodb://"+mongoHost+":"+mongoPuerto+"/"

mongoBD="IECA"                      #se declara la base de datos
mongoColeccion="estudiantes"        #se declara la coleccion
cliente = pymongo.MongoClient(mongoURL, serverSelectionTimeoutMS=mongoTimeout)
baseDatos = cliente[mongoBD]        #se conecta la base de datos y se guarda el objeto
coleccion = baseDatos[mongoColeccion]
idAlumno=""

#------------------------------------------------------------------------------------------------------------------
#*************************************** Funcion para validar correo

def validaCorreo(correoElectronico):
    patron2 = '([a-z0-9_\.-]+)@([\da-z\.]+)\.([a-z\.])'
#El patron consiste en tres secciones
#([a-z0-9_\.-]+) indica que se puede tener un rango de caracteres entre la a - z; un rango de numeros 0 -9;
#un caracater de punto o guion. y con el signo mas de indica que exista uno o mas de estos caracteres

#@ debe de existir un arroba

#([\da-z\.]+) indica que se puede tener un rango de 0-9; un rango de caracteres a-z seguido por un punto y el signo +
#indica que puede tener uno a mas de estos caracteres. Despues sigue un punto.

#([a-z\.]) indica que se puede tener un rango de caracteres entre a-z seguida de un punto
    if re.match(patron2, correoElectronico, re.IGNORECASE):
        return True
    else:
        return False

#***************************************** Funcion para validar nombre
def validaNombre(nombre):
    patron2= '^([aA-zZ ]{1,})([aA-zZ ]{1,})([aA-zZ ]{1,})$'
    if re.match(patron2,nombre, re.IGNORECASE):
        return True
    else:
        return False

#***************************************** Funcion para validar contrasena

def validaPassword(password):
    patron2= '^(?=.*\d)(?=.*[\u0021-\u002b\u003c-\u0040])(?=.*[A-Z])(?=.*[a-z])\S{8,16}$'
    if re.match(patron2,password):
        return True
    else:
        return False
