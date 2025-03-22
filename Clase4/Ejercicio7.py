# Ejercicio 7: Cálculo del área y perímetro
import math

largo = 50
ancho = 100
radio = 5
altura = 7

p_rectangulo = (largo * 2) + (ancho * 2)
a_rectangulo = largo * ancho

p_circulo = 2 * math.pi * radio
a_circulo = math.pi * (radio ** 2)

a_triangulo  = (largo * altura) / 2

resultado = (f"Rectangulo:"
             f"\n\t- Perimetro: {p_rectangulo}"
             f"\n\t- Area: {a_rectangulo}"
             f"\nCirculo:"
             f"\n\t- Perimetro: {p_circulo:.2f}"
             f"\n\t- Area: {a_circulo:.2f}"
             f"\nTriangulo rectangulo:"
             f"\n\t- Area: {a_triangulo}")

print(resultado)