"""NUMERO DE CIFRAS"""
from itertools import count

num = int(input("Introduce un entero: "))

while num != -1:
    if num != 0:
        contador = 0

        while num != 0:
            num //= 10
            contador += 1

        print(f"Numero de cifras: {contador}")
    else:
        print("Numero de cifras: 1")

    num = int(input("Introduce un entero: "))