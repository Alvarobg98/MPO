"""MULTIPLO DE 3 O 5"""

num = input("Introduce un entero positivo: ")

for i in range(int(num)):
    if (i % 3 != 0) or (i % 5 != 0):
        if i % 3 == 0:
            print(f"{i} es multiplo de 3")
        elif i % 5 == 0:
            print(f"{i} es multiplo de 5")