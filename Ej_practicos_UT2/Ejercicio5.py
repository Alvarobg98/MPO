"""
Escribe un programa que pida el nombre de un día de la semana y muestre
si es "laborable" o "fin de semana".
"""

dia = input("Introduce un dia de la semana: ")

if (dia == 'sabado') or (dia == 'domingo'):
    print("Fin de semana")
else:
    print("Laborable")