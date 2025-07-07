"""Escribe un programa que pida el nombre de un día de la semana y muestre si
es "laborable" o "fin de semana"."""
dia = input("Introduce un dia de la semana: ").lower()

if dia in ["sabado", "domingo"]:
    print("Fin de semana")
elif dia in ["lunes", "martes", "miercoles", "jueves", "viernes"]:
    print("Laborable")
else:
    print("Dia incorrecto")