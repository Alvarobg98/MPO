"""Escribe un porgrama que pida un año y muestra si es bisiesto. Un año es
bisiesto si es divisible por 4, pero no por 100, o si es divisible por 400."""

anio = int(input("Introduce un año: "))

if ((anio % 4 == 0) and (anio % 100 != 0)) or (anio % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")