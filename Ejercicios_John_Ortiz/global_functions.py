# Limpiar la consola
import time
import os
import sys

def clear_console():
    time.sleep(2)  # Esperar 2 segundos antes de limpiar la consola
    try:
        # Para Windows
        os.system('cls')
    except:
        # Para Linux y MacOS
        os.system('clear')
    os.system('cls' if os.name == 'nt' else 'clear')