"""NUMEROS PRIMOS"""
import math

num = int(input("Introduce un numero entero: "))

if num >= 2:
    raiz = math.ceil(math.sqrt(num))

    primo = True
    for i in range(2, raiz + 1):
        if num % i == 0:
            primo = False
            break

    if primo:
        print("El numero es primo")
    else:
        print("El numero no es primo")
else:
    print("El numero no es primo")