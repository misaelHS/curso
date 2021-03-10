import socket
import pickle
from estudiante import Estudiante


#-------------------------------------------------ejemplo 3
class cliente:

    def __init__(self, ip='3.16.226.150', puerto=9997):
         #self.ip = '3.16.226.150'
         self.ip=ip
         self.puerto=puerto
         self.conexion=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_DGRAM

    def conectar(self):
         self.conexion.connect((self.ip, self.puerto))

    def desconectar(self):
          self.conexion.close()

    def enviar(self,objeto):
        obj_serializado = pickle.dumps(objeto)

        if isinstance(objeto, Estudiante):
            self.conexion.send(obj_serializado)
            res=self.conexion.recv(1024)
            return res.decode()
        else:
            self.conexion.send(b'INI')
            res=self.conexion.recv(1024)
            print(res.decode())

            if len(obj_serializado)<1024:
                self.conexion.send(obj_serializado)
                #espera respuesta
                res=self.conexion.recv(1024)
                return res.decode()
            else:
                continuar =True
                inicio=0
                while continuar:
                    #toma 1024 byte del objeto serializado
                    chunk = obj_serializado[inicio:inicio+1024]
                    if not  chunk:
                        continuar=False
                        continue

                    self.conexion.send(chunk)
                    res=self.conexion.recv(1024)
                    print(res.decode())

                    inicio +=1024

            self.conexion.send(b'FIN')
            res=self.conexion.recv(1024) # respuesta fin del paquete
            print(res.decode())

            res=self.conexion.recv(1024) #respuesta de validacion del archivo
            return res.decode()


if __name__ == '__main__':
    c=cliente()
    c.conectar()
    e=Estudiante('Misael Hernandez', 'mhernandezs@upbicentenario.edu.mx','12345678')
    r=c.enviar(e)

    print(r)

    f=open('proyecto.zip','rb')
    r=c.enviar(f.read())

    c.desconectar()


#--------------------------------------------------ejemplo 2
#class cliente:

#    def __init__(self, ip='localhost', puerto=9998):
#        #self.ip = '3.16.226.150'
#        self.ip=ip
#        self.puerto=puerto
#        self.conexion=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_DGRAM

#    def conectar(self):
#        self.conexion.connect((self.ip, self.puerto))

#    def desconectar(self):
#        self.conexion.close()

#    def enviar(self,objeto):
#        obj_serializado = pickle.dumps(objeto)
#        self.conexion.send(obj_serializado)

        #espera respuesta
#        res=self.conexion.recv(1024)
#        return res.decode()

#if __name__ == '__main__':
#    c=cliente()
#    c.conectar()
#    e=Estudiante('Misael Hernandez', 'mhernandezs@upbicentenario.edu.mx','12345678')
#    r=c.enviar(e)

#    print(r)

#    f=open('test.zip','rb')
#    r=c.enviar(f.read())

#    c.desconectar()

# ----------------------------------------------- ejemplo 1 para pasar lista
#def main():

#    s=socket.socket()
#    host='3.16.226.150'
#    port=9999

#    s.connect((host,port))
#    estudiante=Estudiante('Misael', 'mhernandezs@upbicentenario.edu.mx', 'misael')
#    estudiante_seriado=pickle.dumps(estudiante)
#    s.send(estudiante_seriado)
#    res=s.recv(1024)
#    print(f'respuesta: \n\t{res.decode()}')
#    s.close()


#if __name__ == '__main__':
#    main()




