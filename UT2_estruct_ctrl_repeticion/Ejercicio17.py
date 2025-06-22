"""CONVERSION BINARIA"""
num = int(input("Introduce un entero positivo: "))

binario = str(num % 2)
num //= 2

while num != 0:
    binario += str(num % 2)
    num //= 2

print("Conversion a binario: ", binario[::-1])