import math

nombre = input("Introduzca su nombre: ")
edad = input("Introduzca su edad: ")
ciudad = input("Introduzca su ciudad: ")

edad_num = int(edad)
if edad_num < 18:
    edad_num = math.ceil(edad_num / 18) * 18

print(f"Nombre: {nombre} - Edad minima: {edad_num} - Ciudad: {ciudad}")