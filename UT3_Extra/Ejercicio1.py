"""Escribe un programa que pida al usuario una lista de números enteros
separados por espacios y un número entero. El programa debe contar cuántas
veces aparece el número en la lista y luego imprimir el resultado."""

lista_num = input("Ingresa una lista de enteros separados por espacios: ")
num = input("¿Que numero quieres contar?: ")

lista_num = lista_num.split()

if num in lista_num:
    cont_num = lista_num.count(num)
    print(f"El numero {num} aparece {cont_num} vez/veces")
else:
    print("El numero especificado no esta en la lista")