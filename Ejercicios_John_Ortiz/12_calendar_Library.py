# Ejercicio 12:

# Ejemplo: mes = 2 | año = 2023

import calendar
import os
import time
from global_functions import clear_console

# Manejo de excepciones para validar que la fecha no esté vacía y sea una fecha válida

try:
    clear_console()
    fecha = str(input("Ingrese el mes y año (mes/año): "))
    print(type(fecha))
    if not fecha.strip():
        raise ValueError("La fecha no puede estar vacía.")
    if '/' not in fecha:
        raise ValueError("La fecha debe contener 2 elementos separados por /")
    if any(not x.strip() for x in fecha.split("/")):
        raise ValueError("Ningún elemento de la fecha puede estar vacío.")
    if any(not x.strip().isdigit() for x in fecha.split("/")):
        raise ValueError("Todos los elementos de la fecha deben ser numéricos.")
    mes, anio = map(int, fecha.split("/"))
    print(type(mes), type(anio))
    if mes < 1 or mes > 12:
        raise ValueError("El mes debe estar entre 1 y 12.")
    if anio < 1900 or anio > 2100:
        raise ValueError("El año debe estar entre 1900 y 2100.")
except ValueError as e:
    print(e)
    clear_console()
    exit()

print(calendar.month(anio, mes))

print("Fin de programa")
print()
# Fin de programa