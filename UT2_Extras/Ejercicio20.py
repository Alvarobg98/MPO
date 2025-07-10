"""Escribe un programa que dado una serie de números introducidos por el
usuario, hasta que introduzca un -1, cuente cuántos de estos números son pares y
cuántos son impares. El programa debe imprimir el número de pares e impares
introducidos, menos el -1."""

num = int(input("Introduce un numero entero: "))
pares = 0
impares = 0

while num != -1:
    if num % 2 == 0:
        pares += 1
    else:
        impares +=1

    num = int(input("Introduce un numero entero: "))

print("Pares: ", pares)
print("Impares: ", impares)
