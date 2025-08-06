"""Escribe un programa que pida al usuario una lista de números enteros
separados por comas. El programa debe definir una función que reciba la lista,
encuentre el máximo y el mínimo de la lista y luego imprima ambos resultados."""

def max_min(lista):
    """Calcula el maximo y el minimo de una lista de enteros"""
    lista.sort()

    maximo = lista[len(lista) - 1]
    minimo = lista[0]

    return maximo, minimo

lista_num = input("Introduce una lista de enteros separados por comas: ")
lista_num = [int(num) for num in lista_num.split(",")]

maxi, mini = max_min(lista_num)
print(f"Maximo: {maxi}"
      f"\nMinimo: {mini}")