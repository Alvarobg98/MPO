"""Escribe un programa que pida al usuario una lista de números enteros
separados por comas. El programa debe eliminar los elementos duplicados
consecutivos de la lista y luego imprimir la lista resultante."""

lista_num = input("Introduce una lista de enteros separados por comas: ")
lista_num = [int(num) for num in lista_num.split(",")]

num_aux = lista_num[0]
lista_aux = [num_aux]
for i in range(1, len(lista_num)):
    if lista_num[i] != num_aux:
        lista_aux.append(lista_num[i])
        num_aux = lista_num[i]

lista_num = lista_aux
print("Lista sin duplicados consecutivos: ", lista_num)