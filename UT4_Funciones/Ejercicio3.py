"""Escribe un programa que pida al usuario un número entero y calcule su
factorial. El programa debe definir una función que reciba el número, realice
el cálculo del factorial y luego imprima el resultado."""

def factorial(numero):
    """Calcula el factorial de un numero"""
    calc_fact = 1

    while numero > 0:
        calc_fact *= numero
        numero -= 1

    return calc_fact

num = int(input("Introduce un entero: "))
fact = factorial(num)

print(f"{num}! = {fact}")