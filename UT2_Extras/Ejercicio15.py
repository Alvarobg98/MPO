"""Escribe un programa que pida al usuario un número entero positivo y calcules
la suma de la potencia de 3 de cada número desde 1 hasta el número introducido.
El programa debe imprimir el resultado. Para que se entienda mejor, si el
usuario introduce 3, el programa debe calcular:
1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36"""

num = int(input("Introduce un entero positivo: "))
suma = 0

for i in range(1, num + 1):
    suma += i ** 3

print(f"Suma: {suma}")
