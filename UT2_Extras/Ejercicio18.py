"""Escribe un programa que dado una serie de números introducidos por el
usuario, hasta que introduzca un -1, imprima el número introducido sumándole 1.
El programa debe imprimir todos los números introducidos, menos el -1,
sumándoles 1."""

num = int(input("Introduce un numero (-1 para salir): "))
serie = []

while num != -1:
    serie.append(num)

    num = int(input("Introduce un numero (-1 para salir): "))

for numero in serie:
    print(numero + 1, end=" ")