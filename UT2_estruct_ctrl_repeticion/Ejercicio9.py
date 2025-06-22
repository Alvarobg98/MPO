"""SUMA ACUMULATIVA"""
num = int(input("Introduce un numero entero: "))
suma = num

while num != 0:
    num = int(input("Introduce un numero entero: "))
    suma += num

print("Suma: ", suma)