"""CONTADOR DE NUMEROS PARES"""

num = input("Introduce un entero positivo: ")
pares = 0

for i in range(0 ,int(num) + 1):
    if i % 2 == 0:
        pares += 1

print(f"Numeros pares desde 0 hasta {num}: {pares}")