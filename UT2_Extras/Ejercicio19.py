"""Escribe un programa que dado una serie de notas introducidas por el usuario,
hasta que introduzca un -1, imprima el número de notas correctas introducidas,
la media de las notas y cuantas de estas notas son 10. El programa debe imprimir
la media de todas las notas introducidas, menos el -1."""

nota = int(input("Introduce una nota (-1 para salir): "))
notas = []

while nota != -1:
    if nota in range(11):
        notas.append(nota)

    nota = int(input("Introduce una nota (-1 para salir): "))

print("\nNotas correctas: ", len(notas))

suma = 0
nota_con10 = 0
for i in notas:
    suma += i

    if i == 10:
        nota_con10 += 1

print("Nota media: ", suma / len(notas))
print("Notas con un 10: ", nota_con10)