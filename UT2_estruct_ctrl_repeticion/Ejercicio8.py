"""CUADRADO CON CRUZ"""
import math

num = input("Introduce un numero entero positivo impar: ")
num = int(num)

if num % 2 == 0 or num < 0:
    print("Error: numero par o negativo")
else:
    for i in range(1, num + 1):
        mitad = math.ceil(num / 2)

        if i == 1 or i == num:
            print("x" * num)
        elif i == mitad:
            for j in range(1, num + 1):
                if (j == 1) or (j == mitad):
                    print("x", end="")
                elif j == num:
                    print("x")
                else:
                    print(" ", end="")
        else:
            for k in range(1, num + 1):
                if k == mitad:
                    print(" ", end="")
                elif k == num:
                    print("x")
                else:
                    print("x", end="")