"""Escribe un programa que pida al usuario un número entero y determine si es
   par o impar. El programa debe imprimir un mensaje indicando el resultado."""
num = int(input("Introduce un numero entero: "))

if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")