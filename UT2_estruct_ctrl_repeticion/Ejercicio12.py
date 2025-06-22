"""MAYOR Y MENOR"""
num = int(input("Introduce un entero: "))
mayor = num
menor = num

while num != 0:
    if num > mayor:
        mayor = num
    elif num < menor:
        menor = num
        
    num = int(input("Introduce un entero: "))

print("El mayor es: ", mayor)
print("El menor es: ", menor)