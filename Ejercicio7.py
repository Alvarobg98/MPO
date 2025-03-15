import random

nombre = input("Introduzca su nombre: ")
random_num = random.randint(0, 9)
passwd = f"{nombre.title()}{random_num}#"

print(f"Contraseña generada: {passwd}")