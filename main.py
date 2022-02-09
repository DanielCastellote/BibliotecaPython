from biblioteca.libro import Libro
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

    def menu():
        usuario1=Usuario("www","Juan")
        usuario2=Usuario("eee","Ana")
        lista_usuarios=[usuario1,usuario2]

        libro1=Libro(3232,"Peter Pan")
        libro2=Libro(8997,"Niño pijama de rayas")
        lista_libros=[libro1,libro2]

        print("Tienes la opcion de hacer 5 acciones diarias:")
        acciones=0
        while(acciones<5):
            print("Elija una opcion")
            opcion=int(input())
            
            if(opcion==1):
                print("Dar de alta 1 socio")
                usuario_alta=Usuario(333,"Ramon","@gmial",54454,"Av","LLL")
                lista_usuarios.append(usuario_alta)
                print("Usuarios actualizados:")
                for usuario in lista_usuarios:
                    print(usuario.nombre)
                
                acciones+=1
            if(opcion==2):
                print("Dar de baja un usuario")
                for usuario in lista_usuarios:
                    print(usuario.nombre)
                print("Elige un usuario segun su numero de la lista teniendo en cuenta que se empieza por 0")
                eliminar= int(input())
                lista_usuarios.remove(lista_usuarios[eliminar])
                print("Usuario eliminado")
                for usuario in lista_usuarios:
                    print(usuario.nombre)

                acciones+=1
            if(opcion==3):
                print("Dar de alta 1 libro")
                libro_alta=Libro(5768,"El Hobbit","pedro","ciencia ficcion","Hobbit","www",4,"Ramon","07/02/2022")
                lista_libros.append(libro_alta)
                print("Libros actualizados:")
                for libro in lista_libros:
                    print(libro.titulo)

                acciones+=1
            if(opcion==4):
                print("Dar de baja un libro")
                for libro in lista_libros:
                    print(libro.titulo)
                print("Elige un libro segun su numero de la lista teniendo en cuenta que se empieza por 0")
                eliminar= int(input())
                lista_libros.remove(lista_libros[eliminar])
                print("Libro eliminado")
                for libro in lista_libros:
                    print(libro.titulo)

                acciones+=1      
            if(opcion==5):
                print("Prestar libros")
            
                acciones+=1





    
    menu()
        

        
        








