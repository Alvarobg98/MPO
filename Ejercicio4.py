nombre_prod = input("Introduce el nombre del producto: ")
precio = input("Introduce su precio: ")

producto = nombre_prod.upper()
precio_format = "{:.2f}".format(float(precio))
codigo = ord(nombre_prod[:1])

print(f"Producto: {producto} - Precio: {precio_format} - Codigo: {codigo}")