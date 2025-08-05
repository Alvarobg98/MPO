"""Escribe un programa que pida al usuario dos listas de números enteros
separados por comas y sume los elementos de ambas listas. Si las listas no
tienen la misma longitud, el programa debe sumar los elementos de la lista
más corta con los elementos correspondientes de la lista más larga y el resto
de los elementos de la lista más larga deben ser sumados a cero. El programa
debe imprimir la lista resultante."""

primera_lista = input("Introduce una lista de enteros separados por comas: ")
segunda_lista = input("Introduce una lista de enteros separados por comas: ")

primera_lista = [int(num) for num in primera_lista.split(",")]
segunda_lista = [int(num) for num in segunda_lista.split(",")]

if len(primera_lista) > len(segunda_lista):
    for i in range(len(segunda_lista)):
        primera_lista[i] += segunda_lista[i]

    print("Lista sumada: ", primera_lista)
else:
    for i in range(len(primera_lista)):
        segunda_lista[i] += primera_lista[i]

    print("Lista sumada: ", segunda_lista)