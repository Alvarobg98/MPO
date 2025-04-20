"""
Escribe un programa que pida una nota (0-10) y muestre:
    "Suspenso" si es menor de 5
    "Aprobado" si es entre 5 y 6
    "Notable" si es entre 7 y 8
    "Sobresaliente" si es 9 o 10
"""
nota = int(input("Introduce tu nota: "))

if (nota >= 5) and (nota <= 6):
    print("Aprobado")
elif (nota >= 7) and (nota <= 8):
    print("Notable")
elif (nota >= 9) and (nota <= 10):
    print("Sobresaliente")
else:
    print("Suspenso")