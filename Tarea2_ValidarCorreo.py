import re           # Se importa la libreria para las expresiones regulares
from Paquete2.Funciones import validaCorreo  # Se importa el modulo de la funcion de validacion

print("\n--------------VALIDACION DE CORREO ELECTRONICO\n\n")
correoElectronico = (input("\n\n Ingrese el correo electronico a validar: "))     # Se solicita, por consola, el numero correo a verificar

print(validaCorreo(correoElectronico)) # Se llama a la funcion pasando por parametros el correo ingresada por consola