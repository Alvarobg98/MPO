"""Escribe un programa que pida día, mes y año. Comprueba si la fecha
introducida es válida. Recuerda que, en los años bisiestos, febrero tiene 29
días. Puedes usar el algoritmo del ejercicio 6 para determinar si un año es
bisiesto."""

dia = int(input("Introduce el dia: "))
mes = int(input("Introduce el mes: "))
anio = int(input("Introduce el año: "))

if ((anio % 4 == 0) and (anio % 100 != 0)) or (anio % 400 == 0):
    # Bisiesto
    if (mes == 2) and (0 < dia <= 29):
        print("Fecha correcta")
    else:
        print("Fecha incorrecta")
else:
    # No es bisiesto
    if (mes in [4, 6, 9, 11]) and (0 < dia <= 30):
        print("Fecha correcta")
    elif (mes in [1, 3, 5, 7, 8, 10, 12]) and (0 < dia <= 31):
        print("Fecha correcta")
    elif (mes == 2) and (0 < dia <= 28):
        print("Fecha correcta")
    else:
        print("Fecha incorrecta")

