"""Escribe un programa que gestione una biblioteca digital utilizando un
diccionario. El programa debe permitir al usuario añadir libros con su título,
autor y año de publicación. El usuario debe poder consultar los libros por autor
o por año de publicación. El programa debe ejecutarse indefinidamente hasta que
el usuario introduzca "SALIR"."""

biblioteca = {}
libro = {}

print("1. Añadir libro"
      "\n2. Consultar por autor"
      "\n3. Consultar por año de publicacion"
      "\n4. SALIR para terminar")

while True:
    opcion = input("Introduce una opcion: ")

    if opcion == '1':
        titulo = input("Introduce el titulo: ")
        autor = input("Introduce el autor: ")
        anio_pub = input("Introduce el año de publicacion: ")

        libro = {"titulo": titulo, "anio": anio_pub}
        biblioteca[autor] = libro
    elif opcion == '2':
        consulta_autor = input("Introduce el nombre del autor: ")

        if consulta_autor in biblioteca:
            print(biblioteca[consulta_autor])
        else:
            print("Autor no encontrado")
    elif opcion == '3':
        consulta_anio = input("Año de publicacion: ")

        for autor, obra in biblioteca.items():
            if consulta_anio in obra.values():
                print(biblioteca[autor])
    elif opcion == "SALIR":
        break