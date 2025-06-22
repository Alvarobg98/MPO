"""BANCA ONLINE"""
print("Bienvenido, realice una operacion:")
print("\t1.Ingresar dinero")
print("\t2.Retirar dinero")
print("\t3.Consultar saldo")
print("\t4.Salir")

opcion = input("\nOpcion: ")
saldo = 0
while opcion != "4":
    if opcion == "1":
        saldo +=  int(input("¿Cuanto desea ingresar?: "))

    if opcion == "2":
        retirar = int(input("¿Cuanto desea retirar?: "))

        if retirar > saldo:
            print("Saldo insuficiente, introduzca otra cantidad")
        else:
            saldo -= retirar

    if opcion == "3":
        print("Saldo: ", saldo)

    opcion = input("\nOpcion: ")
