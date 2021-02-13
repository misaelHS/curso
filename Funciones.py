def funcion(seleccion, maquina_String, opciones_String):      # Se define la funcion que valida los valores a ingresar
    if (seleccion == 1 or seleccion == 2 or seleccion == 3):  # si el numero ingresado por el jugador es 1,2 o 3
        humano_String = opciones_String[seleccion - 1]  # Se crea la variable con la opcione del humano

        print("\t\t\t La maquina dijo: ", maquina_String)  # Se muestra por pantalla la opcion de la maquina
        print("\t\t\t Tu dijiste:\t ", humano_String)  # Se muestra por pantalla la opcion del humano

        if (humano_String == maquina_String):  # si las opcciones son iguales, se tiene un empate y se muestra por pantalla
                    print("\t\t\t Empate")

        elif (humano_String != maquina_String):  # si las opciones son diferentes, se entra a veriricar la posibles combinaciones del juego
            if (humano_String == 'Piedra'):
                if (maquina_String == 'Tijera'):
                    print("\t\t\t Ganaste!")
                if (maquina_String == 'Papel'):
                    print("\t\t\t Perdiste")

            if (humano_String == 'Papel'):
                if (maquina_String == 'Piedra'):
                    print("\t\t\t Ganaste!")
                if (maquina_String == 'Tijera'):
                    print("\t\t\t Perdiste")

            if (humano_String == 'Tijera'):
                if (maquina_String == 'Papel'):
                    print("\t\t\t Ganaste!")
                if (maquina_String == 'Piedra'):
                    print("\t\t\t Perdiste")
    else:
        print("\t\t\t\t\t\t\t ¡Tu eleccion no es correcta!, debe ser un 1, 2 o 3 \n\n ")
        # si el numero ingresado por el jugador no es 1,2 o 3 se le indica que no es correcto


