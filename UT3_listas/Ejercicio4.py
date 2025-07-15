"""Escribe un programa que pida al usuario dos listas de números enteros
separados por comas y sume los elementos de ambas listas. El programa debe
imprimir la lista resultante. Si las listas no tienen la misma longitud, el
programa debe imprimir un mensaje de error."""

lista_1 = input("Introduce una lista de enteros separados por comas: ")
lista_1 = lista_1.split(",")

lista_2 = input("Introduce otra lista de enteros separados por comas: ")
lista_2 = lista_2.split(",")

lista_3 = list()

if len(lista_1) != len(lista_2):
    print("Error: no es posible sumar dos listas de diferente longitud")
else:
    for i in range(len(lista_1)):
        lista_3.append(int(lista_1[i]) + int(lista_2[i]))

    print(lista_3)
