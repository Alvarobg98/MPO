"""Escribe un programa que pida al usuario una lista de números enteros
separados por comas y un número entero. El programa debe definir una función que
reciba la lista y el número, incremente cada elemento de la lista por el número
dado y luego imprima la lista resultante."""

def incremento_lista(num, lista):
    """Incrementa cada elemento de una lista dado un entero"""
    for i in range(len(lista)):
        lista[i] += num

lista_num = input("Introduce una lista de enteros separados por comas: ")
lista_num = [int(n) for n in lista_num.split(",")]

numero = int(input("Introduce un entero: "))

incremento_lista(numero, lista_num)
print("Lista con valores incrementados: ", lista_num)