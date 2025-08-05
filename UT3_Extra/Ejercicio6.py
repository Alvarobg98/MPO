"""Escribe un programa que pida al usuario una lista de números enteros
separados por comas. El programa debe encontrar el segundo valor más grande en
la lista y luego imprimirlo. Si no hay un segundo valor más grande, el programa
debe imprimir un mensaje indicando que no se encontró. Se asegura que la lista
no contiene duplicados."""

lista_num = input("Introduce una lista de enteros separados por comas: ")
lista_num = [int(num) for num in lista_num.split(",")]

lista_aux = []
for num in lista_num:
    if lista_num.count(num) == 1:
        lista_aux.append(num)
    elif num not in lista_aux:
        lista_aux.append(num)

if len(lista_aux) > 1:
    lista_aux.sort(reverse=True)

    print("El segundo valor mas grande es: ", lista_aux[1])
else:
    print("No se ha encontrado el segundo valor mas grande")
