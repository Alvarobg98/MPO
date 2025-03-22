# Ejercicio 9: Fórmula cuadrática
import math

a = 4
b = 12
c = 7

raiz_pos = ( -b + math.sqrt((b**2) - (4*a*c)) ) / (2 * a)
raiz_neg = ( -b - math.sqrt((b**2) - (4*a*c)) ) / (2 * a)

print(f"Ecuacion: {a}x^2 + {b}x + {c}"
      f"\n\t- Solucion 1: {raiz_pos:.3f}"
      f"\n\t- Solucion 2: {raiz_neg:.3f}")

