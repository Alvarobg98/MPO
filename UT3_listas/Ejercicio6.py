"""Escribe un programa que reciba números hasta la introducción de un 0. Por
cada número, suponiendo que el 1 representa el lunes, el 2 el martes, etc.,
imprime el nombre del día correspondiente."""

dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes",
               "sabado", "domingo"]

dia = int(input("Introduce un numero (0 para salir): "))

while dia != 0:
    print(dias_semana[dia - 1])

    dia = int(input("Introduce un numero (0 para salir): "))
