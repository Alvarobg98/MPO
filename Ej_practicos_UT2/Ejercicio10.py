"""
Escribe un programa que pida día, mes y año. Comprueba si la fecha introducida
es válida. Recuerda que, en los años bisiestos, febrero tiene 29 días. Puedes
usar el algoritmo del ejercicio 6 para determinar si un año es bisiesto.
"""
meses = ['enero', 'marzo', 'mayo', 'julio', 'agosto', 'octubre', 'diciembre']
bisiesto = False

dia = int(input("Introduce el dia: "))
mes = input("Introduce el mes: ")
anio = int(input("Introduce el año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    bisiesto = True

if bisiesto and (mes.lower() == 'febrero') and (dia > 29):
    print(f"Fecha invalida: {dia}/{mes}/{anio}")
elif (mes in meses) and (dia > 31):
    print(f"Fecha invalida: {dia}/{mes}/{anio}")
elif (mes not in meses) and (dia > 30):
    print(f"Fecha invalida: {dia}/{mes}/{anio}")
else:
    print(f"Fecha valida: {dia}/{mes}/{anio}")