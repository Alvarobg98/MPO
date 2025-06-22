"""MEDIA DE NOTAS"""
n_eval = int(input("Introduce el numero de evaluaciones: "))

for i in range(n_eval):
    print(f"Notas de la evaluacion {i + 1}")

    nota = float(input("\tIntroduce la siquiente nota: "))
    n_notas = 0
    suma_notas = 0

    while nota != -1:
        n_notas += 1
        suma_notas += nota
        nota = float(input("\tIntroduce la siquiente nota: "))

    print(f"Media de la evaluacion {i + 1}: {(suma_notas / n_notas):.2f}")

