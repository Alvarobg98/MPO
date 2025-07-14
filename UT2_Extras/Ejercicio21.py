"""Escribe un programa que te introduzca un número entero positivo que
corresponde al número de casos a tratar. Seguidamente te introducen un número
entero positivo que corresponde a una serie de números. Después debes recibir
ese total de números e imprimirlos en la misma linea de la terminal, separados
por un espacio y habiéndoles sumado 1 a cada uno de ellos."""

casos = int(input("Introduce un numero de casos (entero positivo): "))
series = []

for _ in range(casos):
    num_serie = int(input("Introduce el tamaño de la serie: "))
    serie = []

    for _ in range(num_serie):
        num = int(input("Introduce un numero: "))
        serie.append(num)

    series.append(serie)
    print()

for n_serie in series:
    for componente_serie in n_serie:
        print(componente_serie + 1, end=" ")

    print()