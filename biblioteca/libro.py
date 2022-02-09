class Libro:
    isbn=0
    titulo=""
    autor=""
    genero=""
    portada=""
    sinopsis=""
    ejemplares=0
    usuario_prestamo="" 
    fecha=""

    def __init__(self,isbn=0,titulo="",autor="",genero="",portada="",sinopsis="",ejemplares=0,usuario="",fecha=""):
        self.isbn=isbn
        self.titulo=titulo
        self.autor=autor
        self.genero=genero
        self.portada=portada
        self.sinopsis=sinopsis
        self.ejemplares=ejemplares
        self.usuario_prestamo=usuario
        self.fecha=fecha

    def imprime_libros(self):
        print(self.isbn,self.titulo,self.autor,self.genero,self.portada,self.sinopsis,self.ejemplares,self.usuario_prestamo,self.fecha)

    
