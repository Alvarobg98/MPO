"""TABLA DE MULTIPLICAR"""

num = input("Introduce un entero positivo: ")

print(f"Tabla de multiplicar del {num}:")

for i in range(1, 11):
    mult = int(num) * i
    print(f"{num} x {i} = {mult}")