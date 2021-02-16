from Paquete2.Funciones import validaCurp  # Se importa el modulo de la funcion de validacion

print("\n--------------VALIDACION DE CURP\n\n")
curp = (input("\n\n Ingrese su CURP a validar: "))     # Se solicita, por consola, la CURP a verificar

print(validaCurp(curp)) # Se llama a la funcion pasando por parametros la CURP ingresada por consola