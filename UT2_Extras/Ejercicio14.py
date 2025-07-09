"""Escribe un programa que pida al usuario un número entero positivo e imprima
la suma de los números pares por un lado y la suma de los números impares por
otro. El programa debe imprimir ambos resultados."""

num = int(input("Introduce un entero positivo: "))
suma_pares = 0
suma_impares = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        # PAR
        suma_pares += i
    else:
        # IMPAR
        suma_impares += i

print("Suma de los pares: ", suma_pares)
print("Suma de los impares: ", suma_impares)