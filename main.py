from re import L
from biblioteca.libro import Libro
from biblioteca.usuario import Usuario
import sys 
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
        ##Usuarios iniciales con libros prestados por defecto
        libro_prestado_1=Libro(3333,"Los tres cerditos","Daniel","Infantil","Contruir casas","Lobo contra cerditos",1,"Juan","20/08/2008")
        usuario1=Usuario("231349K","Juan","juan@gmail",6757382,"Av Alemania",libro_prestado_1)
        usuario2=Usuario("549554P","Ana","ana@gmail",48943434,"Av Polonia")
        lista_usuarios=[usuario1,usuario2]

        #Libros disponibles iniciales
        libro1=Libro(3232,"Peter Pan","Francisco","Aventura","Mundo magico","Historia magica",20,"Usuario1","20/03/2010")
        libro2=Libro(8997,"Niño pijama de rayas","Pedro","Drama","Auswitch","Niño aleman",40,"Usuario3","17/06/2014")
        lista_libros=[libro1,libro2]

        print("Tienes la opcion de hacer 5 acciones diarias:")
        acciones=0
        while(acciones<5):
            print(" ")
            print("Elija una opcion")
            opcion=int(input())
            
            if(opcion==1):
                print("Dar de alta 1 socio")
                print("Indique dni:")
                dni=str(input())
                print("Indique nombre:")
                nombre=str(input())
                print("Indique correo:")
                correo=str(input())
                print("Indique telefono:")
                telefono=int(input())
                print("Indique domicilio:")
                domicilio=str(input())
                print("Indique libros prestados:")
                libros=str(input())
                
                usuario_alta=Usuario(dni,nombre,correo,telefono,domicilio,libros)
                lista_usuarios.append(usuario_alta)
                print(" ")
                print("Usuarios actualizados:")
                for usuario in lista_usuarios:
                    print(usuario.dni,usuario.nombre)
                
                acciones+=1

            if(opcion==2):
                print("Dar de baja un usuario")
                for usuario in lista_usuarios:
                    print(usuario.nombre)
                print("Elige un usuario segun su numero de la lista teniendo en cuenta que se empieza por 0")
                eliminar= int(input())
                lista_usuarios.remove(lista_usuarios[eliminar])
                print(" ")
                print("Usuario eliminado")
                for usuario in lista_usuarios:
                    print(usuario.nombre)

                acciones+=1

            if(opcion==3):
                print("Dar de alta 1 libro:")

                print("Indique isbn:")
                isbn=int(input())
                print("Indique titulo:")
                titulo=str(input())
                print("Indique autor:")
                autor=str(input())
                print("Indique genero:")
                genero=int(input())
                print("Indique portada:")
                portada=str(input())
                print("Indique sinopsis:")
                sinopsis=str(input())
                print("Indique ejemplares:")
                ejemplares=str(input())
                print("Indique usuario:")
                usuario=str(input())
                print("Indique fecha:")
                fecha=str(input())

                libro_alta=Libro(isbn,titulo,autor,genero,portada,sinopsis,ejemplares,usuario,fecha)
                lista_libros.append(libro_alta)
                print(" ")
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
                print(" ")
                print("Libro eliminado")
                for libro in lista_libros:
                    print(libro.titulo)

                acciones+=1     

            if(opcion==5):
                print("Prestar libros")
                print("Indique el libro a prestar segun el numero de la lista teniendo en cuenta que empieza por 0:")
                for libro in lista_libros:
                    print(libro.titulo)
                sacar=int(input())
                print("Indique el usuario a prestar segun el numero de la lista teniendo en cuenta que empieza por 0:")
                for usuario in lista_usuarios:
                    print(usuario.nombre,usuario.libro_prestados)
                prestar=int(input())
                #Sacamos el libro de la lista de libros y se lo insertamos a un usuario sin libro prestado
                lista_usuarios.append(lista_usuarios[prestar].libro_prestados(lista_libros[sacar]))
                lista_libros.remove(lista_libros[sacar])

                print("Libro prestado a",lista_usuarios[prestar].nombre)
                print(lista_usuarios[prestar].libro_prestados)
                acciones+=1

            if(opcion==6):
                print("Devolver libro")
                print("Indique el usuario que quiera devolver alguno de sus libros teniendo en cuenta que empieza por 0")
                for user in lista_usuarios:
                    print(user.nombre)
                devolver=int(input())
                #Sacamos el libro del usuario y lo metemos a la lista de libros de la biblioteca
                libro_devuelto=lista_usuarios[devolver].libro_prestados
                lista_libros.append(libro_devuelto)
                print(libro_devuelto.titulo)
                acciones+=1

            if(opcion==7):
                #Solo saco el titulo, autor y fecha para no sacar un chorro de datos
                print("Consultar libros:")
                for libros in lista_libros:
                    print(libros.titulo,libros.autor,libros.fecha) 

                acciones+=1
            
            if(opcion==8):
                #Solo saco el dni nombre y telefono para no sacar un chorro de datos
                print("Consultar usuario:")
                for usuario in lista_usuarios:
                    print(usuario.dni,usuario.nombre,usuario.telefono)
                acciones+=1
            
            if(opcion==9):
                print("Consultar prestamos:")
                for usuario in lista_usuarios:
                    print(usuario.nombre,"->",usuario.libro_prestados.titulo)
                acciones+=1
            
            if(opcion==10):
                print("FIN")
                acciones=5

        
            
    
    menu()
        

        
        








