"""AKINATOR NUMERICO"""
import random

rand_num = random.randint(1, 100)
num = int(input("Estoy pensando en un numero del 1 al 100, "
                "¿puedes adivinarlo?: "))

while num != rand_num:
    if num < rand_num:
        num = int(input("El numero en el que pienso es mayor: "))
    else:
        num = int(input("El numero en el que pienso es menor: "))

print("¡Enhorabuena, has acertado!")