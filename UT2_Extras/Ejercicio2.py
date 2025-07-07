"""Escribe un programa que pida al usuario un número entero y determine si es
positivo, negativo o cero. El programa debe imprimir un mensaje indicando
el resultado."""
num = int(input("Introduce un numero entero: "))

if num > 0:
    print("El numero es positivo")
elif num < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")