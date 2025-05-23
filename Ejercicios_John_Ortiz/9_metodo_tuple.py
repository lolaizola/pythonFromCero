# Ejercicio 9: Mostrar la fecha de un evento almacenada en una tupla.

# Ejemplo: fecha_evento = (16, 4, 2025)


# Limpiar la consola
import os
import time
from typing import Tuple
from datetime import datetime
from global_functions import clear_console

# Limpiar la consola

# Manejo de excepciones para validar que la fecha no esté vacía y sea una fecha válida

try:
    clear_console()
    fecha = str(input("Ingrese la fecha del evento (dia, mes, año): "))
    print(type(fecha))
    if not fecha.strip():
        raise ValueError("La fecha no puede estar vacía.")
    if ',' not in fecha:
        raise ValueError("La fecha debe contener 3 elementos separados por comas.")
    if any(not x.strip() for x in fecha.split(",")):
        raise ValueError("Ningún elemento de la fecha puede estar vacío.")
    if any(not x.strip().isdigit() for x in fecha.split(",")):
        raise ValueError("Todos los elementos de la fecha deben ser numéricos.")
    dia, mes, anio = map(int, fecha.split(","))
    print(type(dia), type(mes), type(anio))
    if dia < 1 or dia > 31:
        raise ValueError("El día debe estar entre 1 y 31.")
    if mes < 1 or mes > 12:
        raise ValueError("El mes debe estar entre 1 y 12.")
    if anio < 1900 or anio > 2100:
        raise ValueError("El año debe estar entre 1900 y 2100.")
    if mes == 2 and dia > 29:
        raise ValueError("Febrero solo tiene 29 días en años bisiestos.")
    if mes in [4, 6, 9, 11] and dia > 30:
        raise ValueError("Los meses de abril, junio, septiembre y noviembre solo tienen 30 días.")
    if mes == 2 and dia == 29 and not (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
        raise ValueError("El año ingresado no es bisiesto, por lo que febrero solo tiene 28 días.")
    
    fecha_evento = (anio, mes, dia)
    fecha_valida = datetime(anio, mes, dia)
    if fecha != f"{dia},{mes},{anio}":
        raise ValueError("El formato de la fecha ingresada no es válido. Debe ser 'dia,mes,año' sin espacios.")
except ValueError as e:
    print(e)
    clear_console()
    exit()

print("La fecha del evento es: %i%i%i" % fecha_evento)
print()
print("La fecha del evento es: %i/%i/%i" % fecha_evento)
print()
print("La fecha del evento es: {}/{}/{}".format(anio,mes,dia))
print()

print("Fin de programa")
print()
# Fin de programa