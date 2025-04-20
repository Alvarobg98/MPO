"""
Escribe un programa que pida el nombre de un mes y muestre cuántos días tiene
(puedes simplificar febrero a 28 días siempre).
"""
meses = ['enero', 'marzo', 'mayo', 'julio', 'agosto', 'octubre', 'diciembre']
mes = input("Introduce un mes: ")

if mes.lower() in meses:
    print(f"{mes.title()} tiene 31 dias")
elif mes.lower() == 'febrero':
    print("Febrero tiene 28 dias")
else:
    print(f"{mes.title()} tiene 30 dias")