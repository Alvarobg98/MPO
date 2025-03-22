import math

DESCUENTO = 0.85 # Descuento del 15%
precio = input("Introduce el precio del producto: ")

precio_final = int(precio) * DESCUENTO
print(f"Precio final con decimales: {round(precio_final, 2)}")
print(f"Precio final sin decimales: {math.ceil(precio_final)}")