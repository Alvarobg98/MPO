"""Escribe un programa que pida al usuario un número entero positivo e imprima
la lista de divisores de ese número. Un divisor de un número n es un número
entero que divide a n sin dejar residuo. El programa debe imprimir todos los
divisores del número introducido."""

num = int(input("Introduce un numero entero positivo: "))

print(f"Divisores de {num}:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)