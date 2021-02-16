from random import randint  # Se importa la funcion para generar el numero aleatorio de tipo entero
from Paquetes.Funciones import funcion  # Se importa el modulo de la funcion de validacion

numero_int = randint(0, 2)  # Se elije el intervalo [0,2], se tienen tres opciones: 0,1 y 2
opciones_String = ['Piedra', 'Papel', 'Tijera']  # Se crea la tabla de las opciones: piedra, papel y tijeras

print("\n\n\n\n")
print("""------------------------------ Elige un numero para jugar piedra, papel o tijera:  

    ___________ 1 Piedra --------------
    ___________ 2 Papel  --------------
    ___________ 3 Tijera --------------

    """)  # Se crea el menu de las opciones

seleccion = int(input("Digite 1, 2, o 3: "))  # Se realiza una conversion de string a entero del dato de entrada

maquina_String = opciones_String[numero_int]  # Se crea la variable con la opcione de la maquina

funcion(seleccion, maquina_String, opciones_String)  # Se llama a la funcion pasandole parametros para evaluar la opcion

# if __name__=='__main__':

#    funcion(seleccion, maquina_String, opciones_String)
