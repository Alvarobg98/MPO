"""Escribe un programa que pida al usuario dos números enteros e imprima la
secuencia de números entre ellos (incluidos) en orden ascendente. El primer
número siempre será menor que el segundo."""

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))

if num1 < num2:
    for i in range(num1, num2 + 1):
        print(i)
else:
    for i in range(num2, num1 + 1):
        print(i)