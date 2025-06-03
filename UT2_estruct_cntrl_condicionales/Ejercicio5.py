"""
Escribe un programa que pida un rol y una academia de estudios, si el rol es
"alumno" y la academia es "Prometeo" el programa debe darle acceso al servidor
de Discord oficial y al de los alumnos, donde se critica a los profes. Si el rol
es "profesor" y la academia es "Prometeo" el programa debe darle acceso al
servidor de Discord oficial, pero no al de los alumnos. En cualquier otro caso,
el programa debe imprimir "No tienes acceso al servidor de Discord".
"""
rol = input("Introduce si eres 'alumno' o 'profesor': ")
academia = input("Introduce tu academia: ")

if academia != 'Prometeo':
    print("No tienes acceso al servidor de Discord")
elif rol == 'alumno':
    print("Tienes acceso al sevidor oficial y al de alumnos")
else:
    print("Tienes acceso al servidor oficial")