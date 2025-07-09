"""Escribe un programa que pida al usuario un número entero positivo e imprima
la tabla de multiplicar de ese número (del 1 al 10)."""

num = int(input("Introduce un entero positivo: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")