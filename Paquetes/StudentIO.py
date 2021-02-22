from io import open     #Se importa el archivo para manejo de lista
import pickle           #Se importa el archivo para la serializacion


global listaStudentIO   #Se declara una variable global para la lista
listastudentIO = list()


class Estudiante:
    # En este espacio se definen las propiedades, caracteristicas o atributos de la clase
    # Se definen las varaibles clase, por ejemplo:
    #  __nacionalidad=''
    #  __curso=''
    #  __sexo=''
    #  __edad = ''

    # Se definen los comportamientos, metodos o funciones

    def __init__(self, matricula, nombre, nacionalidad, curso, correo,):  # Se define el metodo constuctor de la clase para inicializar las caracteristicas de la clase
        self.matricula = matricula  # Se definen las propiedades del objeto
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.curso = curso
        self.correo = correo

    # Se define el metodo "estudia" que establece el comportamineto del estudiante
    def estudia(self):
        print('\t\t\t El alumno estudia la licenciatura en', self.curso)

    # Se define el metodo "aprende" que establece el comportamineto del estudiante
    def aprende(self):
        print('\t\t\t El alumno aprende los fundamentos de', self.curso)

    # Se define el metodo "practicae" que establece el comportamineto del estudiante
    def practica(self):
        print('\t\t\t El alumno practica la teoria de', self.curso)

    # Se define el metodo "get_datos" que permite obtner los datos del estudiante
    def get_datos(self):
        print("\n")
        print("\t\t\t------------Captura de Datos del Estudiante-------------")
        print("\t\t\tMatricula 4 digitos numericos: ", self.matricula)
        print("\t\t\tNombre: ", self.nombre)
        print("\t\t\tNacionalidad: ", self.nacionalidad)
        print("\t\t\tCurso: ", self.curso)
        print("\t\t\tSexo: ", self.correo)
        print(self.estudia(), self.aprende(), self.practica())
        print("\t\t\t--------------------------------------------")

    # Se define el metodo "set_datos" que permite cambiar los datos del estudiante
    def set_datos(self, matricula, nombre, nacionalidad, curso, correo):
        self.matricula = matricula
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.curso = curso
        self.correo = correo

# -------------------------------------------- MENU ---------------------------------
#--------------------------Funcion de menu para las opciones
def menu():
    opcion = 0

    while opcion != 4:
        print("--------- Menu -----------")
        print("1. Ingresa estudiantes")
        print("2. Muestra estudiantes")
        print("3. Actualiza estudiantes")
        print("4. Salir del menu")
        print("--------------------------")
        opcion = int(input("Ingrese la opcion deseada: "))

        if opcion == 1:
            ingresaEstudiante()
        elif opcion == 2:
            muestraEstudiante()
        elif opcion == 3:
            actualizarEstudientes()
        elif opcion == 4:
            salirMenu()

#-------------------------------------------------Funcion para ingresar los datos del estudiante
def ingresaEstudiante():
    i = 0
    while i <= 4:
        print("\n")
        print("\t\t\t------------Captura de Datos del Estudiante No (",(i+1),")------------")
        matricula = int(input("\t\t\tMatricula 4 digitos numericos: "))
        nombre = input("\t\t\tNombre: ")
        nacionalidad = input("\t\t\tNacionalidad: ")
        curso = input("\t\t\tCurso: ")
        correo = input("\t\t\tcorreo: ")
        a1 = Estudiante(matricula, nombre, nacionalidad, curso, correo)
        listastudentIO.append(a1)
        i=i+1
        print("\n")

    fichero = open('lalistastudentIO.dat', 'wb')       #Se escribe la lista
    pickle.dump(listastudentIO, fichero)
    fichero.close()
    del(fichero)
#-----------------------------------------------------Funcion para mostrar los datos capturados
def muestraEstudiante():
    ficheroOpen = open('lalistastudentIO.dat', "rb")
    listastudentIO = pickle.load(ficheroOpen)
    ficheroOpen.close()
    for c in listastudentIO:
        print(c.get_datos())

#-----------------------------------------------------Funcion para actualizar los datos del estudiante
def actualizarEstudientes():
    i = 0
    while i <= 4:
        print("\n")
        print("\t\t\t------------Actualiza  Datos del Estudiante No (", (i + 1), ")------------")
        matricula = int(input("\t\t\tMatricula 4 digitos numericos: "))
        nombre = input("\t\t\tNombre: ")
        nacionalidad = input("\t\t\tNacionalidad: ")
        curso = input("\t\t\tCurso: ")
        correo = input("\t\t\tcorreo: ")
        a1 = Estudiante(matricula, nombre, nacionalidad, curso, correo)
        listastudentIO.append(a1)
        i = i + 1
        print("\n")

    fichero = open('lalistastudentIO.dat', 'ab')
    pickle.dump(listastudentIO, fichero)
    fichero.close()
    del (fichero)

def salirMenu():
    print("Saliendo del menu ...")

# ----------------------


