"""Escribe un programa que vaya recibiendo cadenas de texto hasta que el usuario
introduzca "fin". El programa debe contar cuántas vocales se han introducido e
imprimir el resultado. Las vocales son: a, e, i, o, u (tanto mayúsculas como
minúsculas). El programa debe imprimir el número total de vocales introducidas
sin contar la palabra "fin"."""

vocales = 0

while True:
    cadena = input("Introduce una cadena de texto: ")

    if cadena.lower() == "fin":
        break
    else:
        for vocal in cadena:
            if vocal.lower() in "aeiou":
                vocales += 1

print("Total de vocales: ", vocales)
