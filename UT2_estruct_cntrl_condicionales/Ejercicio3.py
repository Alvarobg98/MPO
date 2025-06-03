"""
Escribe un programa que pida al usuario dos números enteros correspondientes a
la casilla que está Pacman (1er número) y a la que está un fantasma (2o número),
luego debe recibir un texto con el formato "normal" o "caramelo". Si el texto es
"normal" y los números son iguales, el programa debe imprimir "Pacman ha sido
atrapado". Si el texto es "caramelo" y los números son iguales, el programa debe
imprimir "Pacman ha comido al fantasma". En cualquier otro caso, el programa
debe imprimir "Pacman ha escapado".
"""
casilla_pacman = int(input("Introduce un numero: "))
casilla_fantasma = int(input("Introduce otro numero: "))
texto = input("Introduce 'normal' o 'caramelo': ")

if (casilla_pacman == casilla_fantasma) and (texto == "normal"):
    print("Pacman ha sido atrapado")
elif (casilla_pacman == casilla_fantasma) and (texto == "caramelo"):
    print("Pacman se ha comido al fantasma")
else:
    print("Pacman ha escapado")