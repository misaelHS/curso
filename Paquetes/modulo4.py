
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

