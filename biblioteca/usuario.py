from typing_extensions import Self
from BibliotecaPython.biblioteca.libro import Libro


class Usuario:
    dni=""
    nombre=""
    correo=""
    telefono=0
    domicilio=""
    libro_prestados= Libro()

    def __init__(self,dni="",nombre="",correo="",telefono=0,domicilio="",libros=Libro()):
        self.dni=dni
        self.nombre=nombre
        self.correo=correo
        self.telefono=telefono
        self.domicilio=domicilio
        self.libro_prestados=libros

        