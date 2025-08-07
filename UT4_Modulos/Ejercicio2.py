"""Vamos a evolucionar el programa del ejercicio anterior para que los mensajes
se muestren con colores utilizando el módulo colorama.

Concretamente vamos a modificar la opción de listar archivos.

En vez de imprimir los nombres de los archivos directamente, vamos a colorearlos
según su tipo:
    - Archivos de texto (.txt) en verde.
    - Archivos de imagen (.jpg, .png) en azul.
    - Archivos de audio (.mp3, .wav) en amarillo.
    - Otros archivos en blanco."""
from funciones import *
from os import mkdir

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
        listar_archivo()
    elif opcion == '2':
        file_name = input("¿Que archivo quieres comprobar?: ")
        check_file(file_name)
    elif opcion == '3':
        archivo = input("Nombre del archivo: ")
        check_f = valid_name(archivo)

        if check_f:
            open(archivo, "w")
            print("Archivo creado correctamente\n")
    elif opcion == '4':
        directorio = input("Nombre del directorio: ")
        check_d = valid_name(directorio)

        if check_d:
            mkdir(directorio)
            print("Directorio creado correctamente\n")
