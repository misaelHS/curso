from random import randint                      # Se importa la funcion para generar el numero aleatorio de tipo entero
numero_int=randint(0,2)                         # Se elije el intervalo [0,2], se tienen tres opciones: 0,1 y 2
opciones_String=['Piedra', 'Papel', 'Tijera']   # Se crea la tabla de las opciones: piedra, papel y tijeras


print("""------------------------------ Elige un numero para jugar piedra, papel o tijera:    
    ___________ 1 Piedra 
    ___________ 2 Papel 
    ___________ 3 Tijera 
    """)                                     # Se crea el menu de las opciones

seleccion=int(input("Digite 1, 2, o 3: ")) # Se realiza una conversion de string a entero del dato de entrada

maquina_String= opciones_String[numero_int]  # Se crea la variable con la opcione de la maquina

if(seleccion==1 or seleccion==2 or seleccion==3 ):# si el numero ingresado por el jugador es 1,2 o 3
    humano_String= opciones_String[seleccion-1]   # Se crea la variable con la opcione del humano

    print("\t\t\t La maquina dijo: ", maquina_String)  # Se muestra por pantalla la opcion de la maquina
    print("\t\t\t Tu dijiste:\t ", humano_String)        # Se muestra por pantalla la opcion del humano

    if (humano_String==maquina_String): # si las opcciones son iguales, se tiene un empate y se muestra por pantalla
      print("\t\t\t Empate")

    elif (humano_String!=maquina_String): # si las opciones son diferentes, se entra a veriricar la posibles combinaciones del juego
        if(humano_String=='Piedra'):
            if(maquina_String=='Tijera'):
                print("\t\t\t Ganaste!")
            if(maquina_String=='Papel'):
                print("\t\t\t Perdiste")

        if(humano_String=='Papel'):
            if (maquina_String == 'Piedra'):
                print("\t\t\t Ganaste!")
            if(maquina_String == 'Tijera'):
                print("\t\t\t Perdiste")

        if (humano_String == 'Tijera'):
            if (maquina_String == 'Papel'):
                print("\t\t\t Ganaste!")
            if(maquina_String == 'Piedra'):
                print("\t\t\t Perdiste")
else:
    print("\t\t\t\t\t\t\t Â¡Tu eleccion no es correcta!, debe ser 1, 2 o 3")
    # si el numero ingresado por el jugador no es 1,2 o 3 se le indica que no es correcto

