"""Escribe un programa que pida al usuario una lista de números enteros
separados por comas y la invierta. El programa debe imprimir la lista invertida.
"""

lista = input("Introduce una lista de enteros separados por comas: ")

lista = lista.split(",")
lista.reverse()

print(f"Lista invertida: {lista}")
