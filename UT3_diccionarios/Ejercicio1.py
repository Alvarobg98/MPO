"""Escribe un programa que almacene en un diccionario las capitales de varios
países, se introducirán los datos con la forma PAIS-CAPITAL. Esto debe
ejecutarse indefinidamente hasta que el usuario introduzca "FIN INSERCIONES".
El programa debe permitir al usuario consultar la capital de un país
introduciendo su nombre. Si el país no está en el diccionario, el programa
debe informar al usuario."""

paises = {}

while True:
    pais_capital = input("Introduce un pais-capital (FIN INSERCIONES para "
                         "terminar): ")

    if pais_capital != "FIN INSERCIONES":
        pais_capital = pais_capital.split("-")
        paises[pais_capital[0]] = pais_capital[1]
    else:
        break

while True:
    consulta = input("¿Que pais quieres consultar? (FIN para terminar): ")

    if consulta != "FIN":
        if consulta.lower() in paises:
            print(f"{consulta}: {paises[consulta]}")
        else:
            print("Pais no encontrado")
    else:
        break