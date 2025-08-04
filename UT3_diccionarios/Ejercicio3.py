"""Escribe un programa que gestione un inventario de productos utilizando un
diccionario. El programa debe permitir al usuario añadir productos con su nombre
y cantidad, eliminar productos, y consultar la cantidad de un producto
específico. El programa debe ejecutarse indefinidamente hasta que el usuario
introduzca "SALIR"."""

print("1. Añadir producto"
      "\n2. Eliminar producto"
      "\n3. Consultar cantidad"
      "\n4. SALIR para terminar")

productos = {}
while True:
    opcion = input("Opcion: ")

    if opcion == '1':
        nom_producto = input("Introduce el nombre del producto: ")
        cantidad_prod = input("Introduce la cantidad: ")

        productos[nom_producto] = cantidad_prod
    elif opcion == '2':
        del_producto = input("¿Que producto quieres eliminar?: ")

        del productos[del_producto]
    elif opcion == '3':
        consulta = input("¿Que producto quieres consultar?: ")

        print(f"{consulta}: {productos[consulta]} unidad(es)")
    elif opcion == "SALIR":
        break