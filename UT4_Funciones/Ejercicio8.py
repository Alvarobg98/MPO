"""Escribe un programa que pida al usuario una lista de números enteros
separados por comas. El programa debe definir una función que reciba la lista,
elimine los elementos duplicados y luego imprima la lista resultante."""

def sin_duplicados(lista):
    """Elimina los elementos duplicados de la lista"""
    lista_aux = []

    for n in lista:
        if lista.count(n) == 1:
            lista_aux.append(n)
        elif n not in lista_aux:
            lista_aux.append(n)

    return lista_aux

lista_num = input("Introduce una lista de enteros separados por comas: ")
lista_num = [int(num) for num in lista_num.split(",")]

lista_num = sin_duplicados(lista_num)
print("Lista sin duplicados: ", lista_num)