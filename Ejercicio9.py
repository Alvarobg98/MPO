nombre = input("Introduzca su nombre: ")
apellido = input("Introduzca su apellido: ")

alias = f"{nombre[:3].lower()}{apellido[:3].upper()}"
print(f"Su alias es: {alias}")