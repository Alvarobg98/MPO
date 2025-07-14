"""Escribe un programa que inicialmente te indique el número de casos a tratar.
Después, para cada caso, te introduzca un número entero positivo del cual debes
imprimir todos los divisores. Un divisor de un número n es un número entero que
divide a n sin dejar residuo. El programa debe imprimir todos los divisores del
número introducido en una sola línea, separados por espacios."""

casos = int(input("Numero de casos: "))

for _ in range(casos):
    num = int(input("Introduce un entero positivo: "))
    print(f"Divisores de {num}: ")

    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")

    print("\n")
