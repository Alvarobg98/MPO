"""
Escribe un programa que simule el trabajo de un portero de discoteca.
El programa debe pedir al usuario su edad y determinar si puede entrar o no.
Si la edad es menor de 18 años, el programa debe imprimir "No puedes entrar".
Si la edad es mayor o igual a 18 años, el programa debe imprimir
"Puedes entrar".
"""
edad = input("¿Cuantos años tienes?: ")

if int(edad) < 18:
    print("No puedes entrar")
else:
    print("Puedes entrar")