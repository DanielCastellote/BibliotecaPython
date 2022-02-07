from biblioteca.usuario import Usuario
class Main():
    print(""" Menu interactivo, elige una opcion con el numero asociado a la opcion:
            1º Alta de socio
            2º Baja de socio
            3º Alta de libro
            4º Baja de libro
            5º Prestar libro
            6º Devolver libro
            7º Consultar libros
            8º Consultar usuarios
            9º Consultar prestamos
            10º Salir""")

    def menu(opcion):
        usuario1=Usuario("www","Juan")
        usuario2=Usuario("eee","Ana")
        lista_usuarios=[usuario1,usuario2]
    
        if(opcion==1):
            print("Dar de alta 1 socio")
            usuario_alta=Usuario(333,"Ramon","@gmial",54454,"Av","LLL")
            lista_usuarios.append(usuario_alta)
            print("Usuarios actualizados:")
            for usuario in lista_usuarios:
                print(usuario.nombre)
        



    elegir=int(input())
    menu(elegir)
        

        
        








