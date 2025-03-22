numeros = input("Introduce una lista de numeros separados por comas: ")
numeros = set(map(int, numeros.split(",")))

print(sorted(numeros))