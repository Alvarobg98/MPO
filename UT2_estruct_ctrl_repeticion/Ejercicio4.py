"""FACTORIAL"""

num = input("Introduce un entero positivo: ")
factorial = 1

for i in range(int(num), 0, -1):
    factorial *= i

print(f"El factorial de {num} es: {factorial}")