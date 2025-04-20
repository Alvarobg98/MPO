"""
Escribe un programa que pida dos números y un operador (+, -, *, /)
y muestre el resultado de la operación.
"""
num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))
operador = input("Introduce un operador (+, -, *, /): ")

if operador == '+':
    resultado = num1 + num2
    print(f"Suma: {resultado}")
elif operador == '-':
    resultado = num1 - num2
    print(f"Resta: {resultado}")
elif operador == '*':
    resultado = num1 * num2
    print(f"Multiplicacion: {resultado}")
elif operador == '/':
    resultado = num1 / num2
    print(f"Division: {resultado}")
else:
    print("Operador incorrecto")