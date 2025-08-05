"""Escribe un programa que pida al usuario una lista de números enteros
separados por comas y un número entero. El programa debe eliminar todos los
elementos de la lista que sean mayores al número dado y luego imprimir la lista
resultante."""

lista_num = input("Introduce una lista de enteros separados por comas: ")
num = int(input("Introduce un entero: "))

lista_num = [int(num) for num in lista_num.split(",")]
lista_filtrada = []

for elem in lista_num:
    if elem <= num:
        lista_filtrada.append(elem)

print("Lista actualizada: ", lista_filtrada)