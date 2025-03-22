import random

nombre = input("Introduzca su nombre: ")
apellido = input("Introduzca su primer apellido: ")
usuario = (nombre + apellido).lower()

rand_num = random.randint(1, 10)
usuario = f"{usuario}{rand_num}"

print(f"Nombre de usuario generado: {usuario}")
