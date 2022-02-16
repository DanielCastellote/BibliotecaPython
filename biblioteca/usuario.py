from biblioteca.libro import Libro


class Usuario:
    dni=""
    nombre=""
    correo=""
    telefono=0
    domicilio=""
    libro_prestados= Libro

    def __init__(self,dni="",nombre="",correo="",telefono=0,domicilio="",libros=Libro):
        self.dni=dni
        self.nombre=nombre
        self.correo=correo
        self.telefono=telefono 
        self.domicilio=domicilio
        self.libro_prestados=libros

    def imprime_usuarios(self):
        print(self.nombre,self.dni,self.correo,self.domicilio,self.telefono,self.libro_prestados)
       

        

        