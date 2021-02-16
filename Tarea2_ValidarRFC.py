from Paquete2.Funciones import validaRFC  # Se importa el modulo de la funcion de validacion

print("\n--------------VALIDACION DE RFC\n\n")
rfc = (input("\n\n Ingrese su RFC con homoclave a validar: "))     # Se solicita, por consola, el RFC a verificar

print(validaRFC(rfc)) # Se llama a la funcion pasando por parametros el RFC ingresada por consola