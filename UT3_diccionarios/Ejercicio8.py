"""Escribe un programa que gestione un diccionario de productos, y por cada
producto una lista de ventas diarias representadas como tuplas
(día, unidades_vendidas). Haz un menú que permita al usuario:
    - Añadir un producto con su nombre.
    - Añadir un registro de ventas para un producto específico.
    - Consultar las ventas totales de un producto. El programa debe ejecutarse
    indefinidamente hasta que el usuario introduzca "SALIR".
"""

print("1. Añadir producto"
      "\n2. Añadir registro"
      "\n3. Consultar ventas totales"
      "\n4. SALIR\n")

productos = {}
while True:
    opcion = input("Opcion: ")

    if opcion == "SALIR":
        break
    elif opcion == '1':
        nom_producto = input("Introduce un producto: ")
        productos[nom_producto] = list()
    elif opcion == '2':
        nom_producto = input("Nombre del producto: ")
        lista_ventas = input("Registro de ventas (dia, uni_ven): ")
        lista_ventas = tuple(lista_ventas.split(","))

        productos[nom_producto].append(lista_ventas)
    elif opcion == '3':
        nom_producto = input("Nombre del producto: ")

        suma = 0
        for registro in productos[nom_producto]:
            suma += int(registro[1])

        print("Ventas totales: ", suma)

