"""Escribe un programa que pida el nombre de un mes y muestre cuántos días
tiene (puedes simplificar febrero a 28 días siempre)."""

mes = input("Introduce un mes: ").lower()

if mes in ["abril", "junio", "septiembre", "noviembre"]:
    print("30 dias")
elif mes in ["enero", "marzo", "mayo", "julio", "agosto", "octubre",
             "diciembre"]:
    print("31 dias")
elif mes == "febrero":
    print("28 dias")
else:
    print("No es un mes")