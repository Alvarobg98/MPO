"""
Escribe un programa que pida al usuario un número entero y determine si es
positivo o negativo. El programa debe imprimir un mensaje indicando
el resultado.
"""
num = input("Introduce un numero entero: ")

if int(num) >= 0:
    print(f"El numero {num} es positivo")
else:
    print(f"El numero {num} es negativo")