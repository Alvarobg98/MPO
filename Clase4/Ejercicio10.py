# Ejercicio 10: Manejo y transformación de datos personales
nombre = 'Alvaro'
edad = 26
peso = 85
altura = 1.74

imc = peso / (altura**2)
datos = (f"Nombre: {nombre}"
         f"\nEdad: {edad}"
         f"\nPeso: {peso}"
         f"\nAltura: {altura}"
         f"\nIMC: {imc:.2f}")

print(datos)