"""Escribe un programa que pida al usuario un texto y cuente cuántas veces
aparece cada palabra en el texto. El programa debe imprimir un diccionario donde
las claves son las palabras y los valores son sus respectivas frecuencias.
Ignora la puntuación y considera las palabras en minúsculas."""
import re

conteo = {}
texto = input("Introduce un texto: ")

texto = re.sub(r'[^\w\s]', '', texto)
texto = texto.lower().split()

contador = 0
for i in texto:
    if i not in conteo:
        for j in texto:
            if i == j:
                contador += 1

        conteo[i] = contador

    contador = 0

print(conteo)