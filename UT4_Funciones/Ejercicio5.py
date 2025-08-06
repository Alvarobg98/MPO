"""Escribe un programa que pida al usuario un número entero y calcule la suma
de sus dígitos. El programa debe definir una función que reciba el número,
realice el cálculo de la suma de los dígitos y luego imprima el resultado."""

def suma_dig(num):
    """Calcula la suma de los digitos de un numero"""
    suma = 0

    for i in range(len(num)):
        suma += int(num[i])

    print("Suma de los digitos: ", suma)

numero = input("Introduce un entero: ")
suma_dig(numero)