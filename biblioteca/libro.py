from BibliotecaPython.biblioteca.usuario import Usuario


class Libro:
    isbn=0
    titulo=""
    autor=""
    genero=""
    portada=""
    sinopsis=""
    ejemplares=0
    usuario_prestamo=Usuario()
    fecha=""

    def __init__(self,isbn=0,titulo="",autor="",genero="",portada="",sinopsis="",ejemplares=0,usuario=Usuario,fecha=""):
        self.isbn=isbn
        self.titulo=titulo
        self.autor=autor
        self.genero=genero
        self.portada=portada
        self.sinopsis=sinopsis
        self.ejemplares=ejemplares
        self.usuario_prestamo=usuario
        self.fecha=fecha
