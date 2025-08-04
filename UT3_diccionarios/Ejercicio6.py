"""Escribe un programa que simule unas elecciones a delegado de clase. El
programa debe permitir a los alumnos votar por un candidato introduciendo su
nombre. Al finalizar la votación, el programa debe mostrar el nombre del
candidato ganador y el número de votos obtenidos. Si hay un empate, el programa
debe informar al usuario del primer candidato que alcanzó el número máximo de
votos. El programa debe ejecutarse indefinidamente hasta que el usuario
introduzca "FIN VOTACIONES"."""

candidatos = {}
max_votos = 0
delegado = ""

while True:
    candidato = input("Candidato (FIN VOTACIONES para salir): ")

    if candidato == "FIN VOTACIONES":
        break
    else:
        if candidato not in candidatos:
            candidatos[candidato] = 1
        else:
            candidatos[candidato] = candidatos[candidato] + 1

        if candidatos[candidato] > max_votos:
            max_votos = candidatos[candidato]
            delegado = candidato

print(f"{delegado}: {candidatos[delegado]}")