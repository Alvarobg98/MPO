"""NUMEROS PERFECTOS"""
num = int(input("Introduce un entero positivo: "))
suma_div = 0

for i in range(1, num):
    if num % i == 0:
        suma_div += i

if suma_div == num:
    print("Es un numero perfecto")
else:
    print("No es un numero perfecto")