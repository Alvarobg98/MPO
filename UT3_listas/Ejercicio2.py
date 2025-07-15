"""Escribe un programa que pida al usuario una lista de palabras separadas por
comas y cuente cuántas palabras hay en la lista. El programa debe imprimir el
resultado."""
lista_palabras = input("Introduce una lista de palabras separadas por comas: ")

lista_palabras = lista_palabras.split(",")
print(f"La lista tiene {len(lista_palabras)} palabras")