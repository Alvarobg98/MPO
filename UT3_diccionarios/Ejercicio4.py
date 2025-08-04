"""Escribe un programa que pida al usuario una lista de números enteros
separados por comas y almacene estos números en una tupla. Luego, el programa
debe calcular y mostrar la suma, el promedio, el número máximo y el número
mínimo de la tupla."""

lista_num = input("Introduce numeros enteros separados por comas: ")
lista_num = tuple(lista_num.split(","))

suma = 0
maximo = int(lista_num[0])
minimo = int(lista_num[0])
cont = len(lista_num)

for numero in lista_num:
    numero = int(numero)
    suma += numero

    if numero > maximo:
        maximo = numero
    elif numero < minimo:
        minimo = numero

print("Suma: ", suma)
print("Maximo: ", maximo)
print("Minimo: ", minimo)
print(f"Promedio: {suma / cont}")
