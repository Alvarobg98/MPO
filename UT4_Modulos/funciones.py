from os.path import exists
from os import listdir, stat
from colorama import Fore, Style

def listar_archivo():
    """Lista los archivos del directorio actual"""
    conenido = listdir()
    texto = ".txt"
    imagen_jpg = ".jpg"
    imagen_png = ".png"
    audio_mp3 = ".mp3"
    audio_wav = ".wav"

    print(f"Archivos en el directorio actual: {conenido}")
    for elem in conenido:
        if elem.endswith(texto):
            print(Fore.GREEN + elem + Style.RESET_ALL)
        elif elem.endswith(imagen_jpg) or elem.endswith(imagen_png):
            print(Fore.BLUE + elem + Style.RESET_ALL)
        elif elem.endswith(audio_mp3) or elem.endswith(audio_wav):
            print(Fore.YELLOW + elem + Style.RESET_ALL)
        else:
            print(Fore.WHITE + elem + Style.RESET_ALL)

        print(stat(elem), "\n")

def check_file(nom_archivo):
    """Comrpueba si el archivo existe"""
    if exists(nom_archivo):
        print("El archivo existe\n")
    else:
        print("El archivo no existe\n")

def valid_name(name):
    """Comprueba si el nombre es valido"""
    forbidden_char = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']

    if not name[0].isalnum():
        print("Nombre invalido\n")
        return False
    else:
        for char in name:
            for f_char in forbidden_char:
                if char == f_char:
                    print("Nombre invalido\n")
                    return False

        return True
