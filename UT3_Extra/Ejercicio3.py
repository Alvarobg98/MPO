"""Escribe un programa que pida al usuario una lista de números enteros
separados por comas y filtre los números pares de la lista. El programa debe
imprimir la lista de números pares."""

lista_num = input("Introduce una lista de enteros separados por comas: ")
lista_num = [int(num) for num in lista_num.split(",")]

for num in lista_num:
    if num % 2 != 0:
        lista_num.remove(num)

print(lista_num)

