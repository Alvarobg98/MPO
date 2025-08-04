"""Escribe un programa que replique el comportamiento del ejercicio 1, pero en
lugar de buscar por clave (país), el usuario debe poder buscar por valor
(capital). El programa debe permitir al usuario introducir una capital y
devolver el país correspondiente. Si la capital no está en el diccionario, el
programa debe informar al usuario."""

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
    consulta = input("¿Que capital quieres consultar? (FIN para terminar): ")

    if consulta != "FIN":
        if consulta not in paises.values():
            print("Capital no encontrado")
        else:
            for pais, capital in paises.items():
                if consulta.lower() == capital:
                    print(f"{capital}: {pais}")
    else:
        break