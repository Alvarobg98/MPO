"""
Escribe un programa que pida el precio de un producto y, si supera los 100€,
aplique un descuento del 10%. Muestra el precio final.
"""
precio = int(input("Introduce el precio: "))

if precio > 100:
    descuento = precio * 0.9
    print(f"Total con 10% de descuento: {descuento}")
else:
    print(f"Total sin descuento: {precio}")