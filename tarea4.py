
from Paquetes.modulo4 import *

#----------------------------------------se define la funcion para mostrar datos
def mostrarDatos(nombre="", correo="", materias=""):
    objetoBuscar={} #se crea un objeto de tipo diccionario
    if len(nombre) !=0:#si existe se grega una llave
        objetoBuscar["nombre"]=nombre
    if len(correo) != 0:
         objetoBuscar["correo"]=correo
    if len(materias) !=0:
        objetoBuscar["materias"]=materias
    try:
        registros=tabla.get_children()
        for registros in registros:
            tabla.delete(registros)
        for documento in coleccion.find(objetoBuscar):
            tabla.insert('',0,text=documento["_id"],values=documento["nombre"])
            #print(documento["nombre"]+" "+documento["correo"]+" "+documento["materias"])
            # cliente.server_info()
            # print("Conexion exitosa")
        cliente.close()
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
            print("Tiempo excedido "+errorTiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:
            print("Fallo al conectase "+ errorConexion)


#----------------------------------------se define la funcion para limpiar los campos
def agregarRegistro():
    if(len(nombre.get())!=0 and len(correo.get())!=0 and len(materias.get())!=0):
        try:
            documento={"nombre":nombre.get(), "correo":correo.get(),"materias":materias.get()}
            coleccion.insert_one(documento)
            nombre.delete(0,END)
            correo.delete(0,END)
            materias.delete(0,END)
        except pymongo.errors.ConnectionFailure as error:
            print(error)

    else:
        messagebox.showerror(message="Los campos no pueden estar vacios")
    mostrarDatos()

#----------------------------------------se define la funcion para agregar datos
def dobleClick(event):
    global idAlumno
    idAlumno=tabla.item(tabla.selection())["text"]
    #print(idAlumno)
    documento=coleccion.find({"_id":ObjectId(idAlumno)})[0]
#    print(documento)
    nombre.delete(0,END)
    nombre.insert(0,documento["nombre"])
    correo.delete(0, END)
    correo.insert(0, documento["correo"])
    materias.delete(0, END)
    materias.insert(0, documento["materias"])
    agregar["state"]="disabled"
    editar["state"] = "disabled"
    borrar["state"] = "normal"

#----------------------------------------se define la funcion para editar datos
def editarRegistro():
    global idAlumno
    if (len(nombre.get()) != 0 and len(correo.get()) != 0 and len(materias.get()) != 0):
        try:
            idBuscar={"_id":ObjectId(idAlumno)}
            actualizarValores={"nombre": nombre.get(), "correo": correo.get(), "materias": materias.get()}
            coleccion.update(idBuscar,actualizarValores)
            nombre.delete(0, END)
            correo.delete(0, END)
            materias.delete(0, END)
        except pymongo.errors.ConnectionFailure as error:
            print(error)

    else:
        messagebox.showerror(message="Los campos no pueden estar vacios")
    mostrarDatos()
    agregar["state"] = "normal"
    editar["state"] = "disabled"
    borrar["state"] = "disabled"

#----------------------------------------se define la funcion para borrar datos
def borrarRegistro():
    global idAlumno
    try:
        idBuscar = {"_id": ObjectId(idAlumno)}
        coleccion.delete_one(idBuscar)
        nombre.delete(0, END)
        correo.delete(0, END)
        materias.delete(0, END)
    except pymongo.errors.ConnectionFailure as error:
          print(error)

    mostrarDatos()
    agregar["state"] = "normal"
    editar["state"] = "disabled"
    borrar["state"] = "disabled"

#----------------------------------------se define la funcion para buscar datos
def buscarRegistro():
    mostrarDatos(bucarNombre.get(), buscarCorreo.get(), buscarMaterias.get())

#.-----------

#---------------------------------------configuracion de interfaz grafica
ventana=Tk()
tabla=ttk.Treeview(ventana,columns=3)
tabla.grid(row=1,column=0,columnspan=3)
tabla.heading("#0",text="ID")
tabla.heading("#1",text="NOMBRE")
#tabla.heading("#2",text="CORREO")
#tabla.heading("#3",text="MATERIAS")
tabla.bind("<Double-Button-1>",dobleClick)
#iterfaz grafica para agregar el nombre
Label(ventana,text="Nombre").grid(row=2,column=0,sticky=W+E)
nombre=Entry(ventana)
nombre.grid(row=2,column=1,sticky=W+E)
nombre.focus()
#interfaz grafica para agregar el correo
Label(ventana,text="Correo").grid(row=3,column=0,sticky=W+E)
correo=Entry(ventana)
correo.grid(row=3,column=1,sticky=W+E)
#interfaz para agregar la materia
Label(ventana,text="Materias").grid(row=4,column=0,sticky=W+E)
materias=Entry(ventana)
materias.grid(row=4,column=1,sticky=W+E)
#interfaz para el icono Agregar
agregar=Button(ventana, text="Agregar estudiante", command=agregarRegistro, bg="blue", fg="white")
agregar.grid(row=5,column=2,sticky=W+E)
#interfaz para el icono Editar
editar=Button(ventana,text="Editar estudiante", command=editarRegistro, bg="yellow")
editar.grid(row=6,column=2,sticky=W+E)
editar["state"]="disabled"
#interfaz para el icono Borrar
borrar=Button(ventana,text="Borrar estudiante", command=borrarRegistro, bg="red", fg="white")
borrar.grid(row=7,column=2,sticky=W+E)
borrar["state"]="disabled"

# Configuracion de la interfaz grafica para el boton buscar datos en la base
buscar=Button(ventana,text="Buscar datos", command=buscarRegistro, bg="green", fg="white")
buscar.grid(row=8,column=2,sticky=W+E)
#interfaz para buscar el nombre
Label(ventana,text="Buscar por nombre").grid(row=9,column=0,sticky=W+E)
bucarNombre=Entry(ventana)
bucarNombre.grid(row=9,column=1,sticky=W+E)
nombre.focus()
#interfaz para buscar el correo
Label(ventana,text="Buscar por correo").grid(row=10,column=0,sticky=W+E)
buscarCorreo=Entry(ventana)
buscarCorreo.grid(row=10,column=1,sticky=W+E)
#interfaz para buscar la materia
Label(ventana,text="Buscar por materias").grid(row=11,column=0,sticky=W+E)
buscarMaterias=Entry(ventana)
buscarMaterias.grid(row=11,column=1,sticky=W+E)
mostrarDatos()
ventana.mainloop()



