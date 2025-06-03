"""
Escribe un programa que pida al usuario un número entero y determine si es
múltiplo de 3 o de 5. El programa debe imprimir un mensaje indicando el
resultado. Si el número es múltiplo de ambos, debe imprimir "Múltiplo de 3 y 5".
Si no es múltiplo de ninguno, debe imprimir "No es múltiplo de 3 ni de 5".
"""
num = int(input("Introduce un numero entero: "))

if (num % 5 == 0) and (num % 3 == 0):
    print("Multiplo de 3 y 5")
elif num % 5 == 0:
    print("Multiplo de 5")
elif num % 3 == 0:
    print("Multiplo de 3")
else:
    print("No es multiplo de 3 ni de 5")