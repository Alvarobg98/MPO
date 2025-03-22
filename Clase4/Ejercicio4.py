# Ejercicio 4: Índices y subcadenas
cadena = ("Primero aprendi a programar en C++, despues aprendi Java"
          " y por ultimo estoy aprendiendo Python")
cadena_nueva = cadena[31:34] + ", " + cadena[51:56] + ", " + cadena[-7:]

print(cadena_nueva[::-1])