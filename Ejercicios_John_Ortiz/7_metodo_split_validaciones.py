# Ejercicio 7: Obtener la extension de un archivo especificado por el usuario
# Instrucciones:

# Ejemplo: main.py

import os
import time
from typing import List
from global_functions import clear_console

# Manejo de excepciones para validar que la cadena no esté vacía y sea un nombre de archivo válido

try:
    clear_console()
    archivo = str(input("Ingrese el nombre del archivo (con extension): "))
    if not archivo.strip():
        raise ValueError("El nombre del archivo no puede estar vacío.")
    if '.' not in archivo:
        raise ValueError("El nombre del archivo debe contener un punto para indicar la extensión.")
    if archivo.split(".")[-1] == "":
            raise ValueError("La extensión del archivo no puede estar vacía.")
except ValueError as e:
    print(e)
    clear_console()
    exit()

# Validar que el nombre del archivo contenga mas de un punto

if archivo.count(".") > 1:
    nombre_archivo = ".".join(archivo.split(".")[:-1])
    extension_archivo = archivo.split(".")[-1]
    print("El nombre del archivo es:", nombre_archivo)
    print("La extensión del archivo es:", extension_archivo)
    exit()
else:
    print("El nombre del archivo es:", archivo.split(".")[0])
    print()
    print("La extensión del archivo es:", archivo.split(".")[-1])
    exit()

print()

print("Fin de programa")
print()
# Fin de programa