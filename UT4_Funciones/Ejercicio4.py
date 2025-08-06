"""Escribe un programa que pida al usuario un número entero y verifique si es
primo. El programa debe definir una función que reciba el número, realice la
verificación y luego imprima si el número es primo o no."""

def es_primo(num):
    """Comrpueba si un numero es primo"""
    verificacion = True

    for divisor in range(2, num):
        if num % divisor == 0:
            verificacion = False
            break

    if verificacion:
        print("Es primo")
    else:
        print("No es primo")

numero = int(input("Introduce un entero: "))
es_primo(numero)