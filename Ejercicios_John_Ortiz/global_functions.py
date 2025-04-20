# Obtener librerías necesarias

from datetime import datetime
import os
import sys
import time

# Función para limpiar la consola
def clear_console():
    time.sleep(2)  # Esperar 2 segundos antes de limpiar la consola
    try:
        # Para Windows
        os.system('cls')
    except OSError:
        # Para Linux y MacOS
        os.system('clear')
    os.system('cls' if os.name == 'nt' else 'clear')


# Función para validar los valores ingresados
def validar_fecha(fecha_str):
    try:
        validar_formato_basico(fecha_str)
        dia, mes, anio = map(int, fecha_str.split("/"))
        validar_rangos(dia, mes, anio)
        validar_fecha_especifica(dia, mes, anio)
        return datetime(anio, mes, dia)  # Retorna el objeto datetime si es válido
    except ValueError as e:
        print()
        print(f"Error: {e}")
        print()

# Función para validar el formato basico de la fecha
# (dd/mm/yyyy) y verificar que no esté vacía
def validar_formato_basico(fecha_str):
    if not fecha_str.strip():
        raise ValueError("La fecha no puede estar vacía.")
    elementos = fecha_str.split("/")
    if len(elementos) != 3:
        raise ValueError("La fecha debe contener 3 elementos separados por '/'.")
    if any(not x.strip() for x in elementos):
        raise ValueError("Ningún elemento de la fecha puede estar vacío.")
    dia, mes, anio = elementos
    if len(dia) != 2 or len(mes) != 2 or len(anio) != 4:
        raise ValueError("El formato de la fecha debe ser dd/mm/yyyy.")
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        raise ValueError("Todos los elementos de la fecha deben ser numéricos.")

# Función para validar los rangos de la fecha
# (día entre 1 y 31, mes entre 1 y 12, año entre 1900 y 2100)
def validar_rangos(dia, mes, anio):
    if not (1 <= dia <= 31):
        raise ValueError("El día debe estar entre 1 y 31.")
    if not (1 <= mes <= 12):
        raise ValueError("El mes debe estar entre 1 y 12.")
    if anio < 1900 or anio > 2100:
        raise ValueError("El año debe estar entre 1900 y 2100.")

# Función para validar fechas específicas
# (por ejemplo, febrero no puede tener más de 29 días, abril no puede tener más de 30 días, etc.)
def validar_fecha_especifica(dia, mes, anio):
    if mes in [4, 6, 9, 11] and dia > 30:
        raise ValueError("El mes ingresado no puede tener más de 30 días.")
    if mes == 2:
        if dia > 29:
            raise ValueError("Febrero no puede tener más de 29 días.")
        if dia == 29 and not (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
            raise ValueError("El año ingresado no es bisiesto, por lo que febrero solo tiene 28 días.")