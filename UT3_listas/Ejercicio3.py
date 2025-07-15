"""Escribe un programa que pida al usuario una lista de números enteros
separados por comas y encuentre el mayor y el menor elemento de la lista. El
programa debe imprimir ambos resultados."""

lista_num = input("Introduce una lista de enteros separados por comas: ")

lista_num = lista_num.split(",")

for i in range(len(lista_num)):
    lista_num[i] = int(lista_num[i])

lista_num.sort()
print(f"El menor elemento es el {lista_num[0]} y el mayor "
      f"es el {lista_num[len(lista_num) - 1]}")