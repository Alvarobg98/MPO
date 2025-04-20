"""
Escribe un programa que pida al usuario un número entero y determine si es
divisible por 3 y 5. El programa debe imprimir un mensaje indicando el resultado
"""
num = int(input("Introduce un numero entero: "))

if (num % 3 == 0) and (num % 5 == 0):
    print("El numero es divisible por 3 y 5")
else:
    print("El numero no es divisible tanto por 3 como por 5")