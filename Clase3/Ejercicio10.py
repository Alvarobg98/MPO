import math

numero = input("Introduce un numero decimal: ")
numero = float(numero)

print(f"Numero: {round(numero, 2)}")
print(f"\t- Cuadrado: {numero**2}")
print(f"\t- Raiz cuadrada: {math.sqrt(numero)}")