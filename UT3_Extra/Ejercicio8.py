"""Escribe un programa que pida al usuario una lista de números enteros
separados por comas. El programa debe eliminar los elementos duplicados de la
lista y luego imprimir la lista resultante."""

lista_num = input("Introduce una lista de enteros separados por comas: ")
lista_num = [int(num) for num in lista_num.split(",")]

lista_aux = []
for num in lista_num:
    if lista_num.count(num) == 1:
        lista_aux.append(num)
    elif num not in lista_aux:
        lista_aux.append(num)

lista_num = lista_aux
print("Lista sin duplicados: ", lista_num)