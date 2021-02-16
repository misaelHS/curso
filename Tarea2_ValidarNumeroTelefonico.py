from Paquete2.Funciones import validaNumeroTelefonico  # Se importa el modulo de la funcion de validacion

print("\n--------------VALIDACION DE NUMERO TELEFONICO EN DOS FORMATOS a 10 DIGITOS: 5551383552 o (555)1383552\n\n")
numeroTelefonico = (input("\n\n Ingrese el numero telefonico a validar: "))     # Se solicita, por consola, el numero telefonico a verificar

print(validaNumeroTelefonico(numeroTelefonico)) #Se llama a la funcion pasando por parametros el numero ingresado por consola
