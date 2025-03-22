invitados = ['Alvaro', 'Mario', 'Elena', 'Jorge']
nombre = input("Introduzca su nombre: ")

if nombre.title() in invitados:
    print(f"{nombre.title()}, usted se encuentra en la posicion {invitados.index(nombre.title())} de la lista")
else:
    print(f"El usuario {nombre.title()} no se encuentra en la lista")