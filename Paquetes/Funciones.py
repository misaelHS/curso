import re           # Se importa la libreria para las expresiones regulares

#---------------------------------------- TAREA1: FUNCION DE PIEDRA PAPEL Y TIJERAS ------------------------------------------------

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


#-------------------------------------------- TAREA 2: FUNCIONES PARA VALIDAR PATRONES REGULARES -------------------------------


#-----------------------------------------------------------------------------
def validaNumeroTelefonico(numeroTelefonico):     # FUNCION PARA VALIDAR EL NUMERO TELEFONICO EN LA TAREA 2
                                            #Se crea la funcion a evaluar el el formato del numero telefonico

    patron1='^\(?\d{3}?(\)?\d{7}?)$'        # Se establece el patron, dentro de la cadena de carateres limitada con ^$.
                                            # (? \d{d3} ? Puede o no contener el simbolo (, despues deben de ir 3 digitos enteros
                                            # ( \)?\d{7}? ) en la segunda seccion limitada por parentesis se indica que puede o no
                                            # ir el simbolo del parentesis cerrado ) y depues deben ir 7 digitos

    if re.match(patron1,numeroTelefonico) : # Se evalua el patron del numero telefonico mediante la expresion regular macht
        print('\n\n\n \t\t\t\t\t El numero es correcto \n\n')
    else:
        print('\n\n\n \t\t\t\t\t El numero no es correcto \n\n')


#------------------------------------------------------------------------------

def validaCorreo(correoElectronico):                # FUNCION PARA VALIDAR EL CORREO EN LA TAREA 2
    patron2 = '([a-z0-9_\.-]+)@([\da-z\.]+)\.([a-z\.])'
#El patron consiste en tres secciones
#([a-z0-9_\.-]+) indica que se puede tener un rango de caracteres entre la a - z; un rango de numeros 0 -9;
#un caracater de punto o guion. y con el signo mas de indica que exista uno o mas de estos caracteres

#@ debe de existir un arroba

#([\da-z\.]+) indica que se puede tener un rango de 0-9; un rango de caracteres a-z seguido por un punto y el signo +
#indica que puede tener uno a mas de estos caracteres. Despues sigue un punto.

#([a-z\.]) indica que se puede tener un rango de caracteres entre a-z seguida de un punto

    if re.match(patron2, correoElectronico, re.IGNORECASE):     # Se define la bandera para ignorar mayusculas del correo
        print('El correo es correcto')
    else:
        print('El correo no es correcto')

#-----------------------------------------------------------------------------------------

def validaCurp(curp):                      # FUNCION PARA VALIDAR EL CURP EN LA TAREA 2
    patron2 = '^([a-z]{4})([0-9]{6})([MH]{1})([a-z]{2})([a-z]{3})([\d]{2})$' # se define el patron de la curp
    if re.match(patron2,curp, re.IGNORECASE):
        print('La CURP es correcta')
    else:
        print('La CURP no es correcta')

#------------------------------------------------------------------------------------------

def validaRFC(rfc):                         # FUNCION PARA VALIDAR EL RFC EN LA TAREA 2
    patron2 = '^([a-z]{4})([0-9]{6})([a-z0-9]{3})$' # se define el patron del rfc
    if re.match(patron2,rfc, re.IGNORECASE):
        print('El RFC es correcto')
    else:
        print('El RFC no es correcto')