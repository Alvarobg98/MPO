"""Escribe un programa que pida al usuario una lista de números enteros
separados por comas y calcule la suma de todos los elementos de la lista. El
programa debe imprimir el resultado."""

lista = input("Introduce una serie de enteros separados por comas: ")
suma = 0

lista = lista.split(",")
for elem in lista:
    suma += int(elem)

print(f"La suma de los elementos es: {suma}")




