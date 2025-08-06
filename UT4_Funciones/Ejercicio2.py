"""Escribe un programa que pida al usuario un nombre, un apellido y una edad.
El programa debe definir una función que reciba estos datos y luego imprima un
mensaje de bienvenida personalizado."""

def mensaje_pers(nom, apell, anios):
    """Imprime un mensaje personalizado"""
    print(f"Bienvenido {nom} {apell} {anios}")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")

mensaje_pers(nombre, apellido, edad)