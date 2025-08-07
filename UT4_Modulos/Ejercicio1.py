"""Desarrollar un programa en Python que permita gestionar archivos y
directorios mediante un menú interactivo, utilizando las funciones principales
del módulo os."""

from os.path import exists
from os import listdir, mkdir

while True:
    print("1. Listar archivos"
               "\n2. Verificar si un archivo existe"
               "\n3. Crear archivo"
               "\n4. Crar directorio"
               "\n5. Salir\n")
    opcion = input("Introduce una opcion (numero): ")

    if opcion == '5':
        break
    elif opcion == '1':
        conenido = listdir()
        print(f"Archivos en el directorio actual: {conenido}\n")
    elif opcion == '2':
        check_file = input("¿Que archivo quieres comprobar?: ")

        if exists(check_file):
            print("El archivo existe\n")
        else:
            print("El archivo no existe\n")
    elif opcion == '3':
        forbidden_char = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
        archivo = input("Nombre del archivo: ")

        if not archivo[0].isalnum():
            print("Nombre de archivo invalido\n")
        else:
            check = True

            for char in archivo:
                for f_char in forbidden_char:
                    if char == f_char:
                        print("Nombre de archivo invalido\n")
                        check = False

                        break

            if check:
                open(archivo, "w")
                print("Archivo creado correctamente\n")
    elif opcion == '4':
        directorio = input("Nombre del directorio: ")
        forbidden_char = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']

        if not directorio[0].isalnum():
            print("Nombre de directorio invalido\n")
        else:
            check = True

            for char in directorio:
                for f_char in forbidden_char:
                    if char == f_char:
                        print("Nombre de directorio invalido\n")
                        check = False

                        break

            if check:
                mkdir(directorio)
                print("Directorio creado correctamente\n")
