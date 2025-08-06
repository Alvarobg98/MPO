"""Escribe un programa que pida al usuario el radio de un círculo y calcule su
área. El programa debe definir una función que reciba el valor del radio,
realice el cálculo del área y luego imprima el resultado."""
from math import pi, pow
def calc_area_circ(radio):
    """Calcula el area de un circulo"""
    area = pi * pow(radio, 2)

    return area

r = int(input("Introduce el radio del circulo: "))
a = calc_area_circ(r)

print(f"El area del circulo es: {a:.2f}")