# Ejercicio 8: Análisis de texto complejo
parrafo = ("\tLorem ipsum dolor sit amet, consectetur adipiscing elit. Donec"
           "\n ornare arcu augue, quis blandit dui facilisis quis. Mauris quis"
           "\n sapien aliquam, consequat libero id, blandit sem. Quisque et"
           "\n velit ac libero faucibus fermentum non in nisi. Nunc felis"
           "\n massa, suscipit et urna et, sollicitudin tincidunt magna. Nam"
           "\n imperdiet in neque id luctus. Nullam egestas venenatis magna et"
           "\n varius. Morbi elementum porttitor nisl, sed congue lacus sodales"
           "\n id. Fusce euismod est magna, mattis bibendum justo euismod quis."
           "\n Aliquam lobortis varius dui non cursus. Phasellus id orci magna."
           "\n Etiam quis tincidunt nisl.")

caracteres = len(parrafo)
palabras = len(parrafo.split())
parrafo_upper = parrafo.upper()

print(f"Numero de caracteres: {caracteres}"
      f"\nNumero de palabras: {palabras}"
      f"\nParrafo en mayusculas:"
      f"\n{parrafo_upper}")