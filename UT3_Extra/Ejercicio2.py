"""Escribe un programa que pida al usuario una lista de números enteros
separados por espacios y un número entero. El programa debe multiplicar todos
los elementos de la lista por el número dado y luego imprimir la lista
resultante."""

lista_num = input("Introduce una lista de enteros separados por espacios: ")
mult_num = input("¿Por que numero quieres multiplicar?: ")

lista_num = lista_num.split()
lista_mult = []

for num in lista_num:
    lista_mult.append(int(num) * int(mult_num))

print(lista_mult)