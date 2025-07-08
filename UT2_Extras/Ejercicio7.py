"""Escribe un programa que pida dos números y un operador (+, -, *, /)
y muestre el resultado de la operación."""

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))
opertacion = input("Operador (+, -, *, /): ")

if opertacion == '+':
    result = num1 + num2
    print(f"{num1} {opertacion} {num2} = {result}")
elif opertacion == '-':
    result = num1 - num2
    print(f"{num1} {opertacion} {num2} = {result}")
elif opertacion == '*':
    result = num1 * num2
    print(f"{num1} {opertacion} {num2} = {result}")
elif opertacion == '/':
    result = num1 / num2
    print(f"{num1} {opertacion} {num2} = {result}")
else:
    print("Operador incorrecto")