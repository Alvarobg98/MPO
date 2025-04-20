"""
Escribe un porgrama que pida un año y muestra si es bisiesto. Un año es bisiesto
 si es divisible por 4, pero no por 100, o si es divisible por 400.
"""
anio = int(input("Introduce un año: "))

if (anio % 100 == 0) and (anio % 400 == 0):
    print("El año es bisiesto")
elif (anio % 4 == 0) and (anio % 100 != 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")