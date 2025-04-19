# Ejercicio 14: Calcular la diferencia en dias entre dos fechas obtenidas por pantalla.

# Ejemplo:
            #hoy = datetime.date.today()
            #fecha_anterior= 10/4/2025

# Obtener las librerias necesarias

# import os
# import time
# from datetime import datetime, timedelta

# Limpiar la consola

# def clear_console():
#     time.sleep(2)  # Esperar 2 segundos antes de limpiar la consola
#     try:
#         # Para Windows
#         os.system('cls')
#     except:
#         # Para Linux y MacOS
#         os.system('clear')
#     os.system('cls' if os.name == 'nt' else 'clear')

# # Manejo de excepciones para validar que la fecha no esté vacía, sea una fecha válida y la segunda fecha sea menor a la primera


# try:
#     clear_console()
#     fecha = str(input("Ingrese la fecha (dd/mm/yyyy): "))
#     print(type(fecha))
#     if not fecha.strip():
#         raise ValueError("La fecha no puede estar vacía.")
#     if '/' not in fecha:
#         raise ValueError("La fecha debe contener 3 elementos separados por /")
#     if any(not x.strip() for x in fecha.split("/")):
#         raise ValueError("Ningún elemento de la fecha puede estar vacío.")
#     if any(not x.strip().isdigit() for x in fecha.split("/")):
#         raise ValueError("Todos los elementos de la fecha deben ser numéricos.")
#     dia, mes, anio = map(int, fecha.split("/"))
#     print(type(dia), type(mes), type(anio))
#     if dia < 1 or dia > 31:
#         raise ValueError("El día debe estar entre 1 y 31.")
#     if mes < 1 or mes > 12:
#         raise ValueError("El mes debe estar entre 1 y 12.")
#     if dia > 30 and mes in [4, 6, 9, 11]:
#         raise ValueError("Los meses de abril, junio, septiembre y noviembre no pueden tener más de 30 días.")
#     if dia > 31 and mes in [1, 3, 5, 7, 8, 10, 12]:
#         raise ValueError("Los meses de enero, marzo, mayo, julio, agosto, octubre y diciembre no pueden tener más de 31 días.")
#     if mes == 2 and dia > 29:
#         raise ValueError("Febrero no puede tener más de 29 días.")
#     else:
#         if mes == 2 and dia == 29 and not (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
#             raise ValueError("El año ingresado no es bisiesto, por lo que febrero solo tiene 28 días.")
#         else:
#             if dia > 28 and mes == 2:
#                 raise ValueError("El mes de febrero no puede tener más de 28 días.")
#     if anio < 1900 or anio > 2100:
#         raise ValueError("El año debe estar entre 1900 y 2100.")

# except ValueError as e:
#     print(e)
#     clear_console()
#     exit()

#######################################3

import os
import time
from datetime import datetime
from global_functions import clear_console

# Función para limpiar la consola
def clear_console():
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")

# Función para validar los valores ingresados
def validar_fecha(fecha_str):
    try:
        clear_console()
        
        # Verifica que tenga el formato correcto y extrae los valores
        
        elementos = fecha_str.split("/")
        if len(elementos) != 3:
            raise ValueError("La fecha debe contener 3 elementos separados por '/'.")

        dia, mes, anio = elementos

        # Validar que el formato sea dd/mm/yyyy y no yyyy/mm/dd
        if len(dia) != 2 or len(mes) != 2 or len(anio) != 4:
            raise ValueError("El formato de la fecha debe ser dd/mm/yyyy.")
        
        # Validar que sean valores numéricos
        if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
            raise ValueError("Todos los elementos de la fecha deben ser numéricos.")
            
            
        dia, mes, anio = map(int, elementos)

        # Restricciones de rango
        if not (1 <= dia <= 31):
            raise ValueError("El día debe estar entre 1 y 31.")
        if not (1 <= mes <= 12):
            raise ValueError("El mes debe estar entre 1 y 12.")
        if not (1900 <= anio <= 2100):
            raise ValueError("El año debe estar entre 1900 y 2100.")

        # Validación usando `datetime`
        fecha_obj = datetime(anio, mes, dia)
        return fecha_obj  # Retorna el objeto datetime si es válido

    except ValueError as e:
        print(f"Error: {e}")
        return None  # Retorna None si la validación falla

# Función para calcular diferencia de días
def calcular_diferencia(fecha_str):
    fecha_validada = validar_fecha(fecha_str)
    if fecha_validada:
        fecha_actual = datetime.today()
        diferencia_dias = (fecha_actual - fecha_validada).days
        print(f"La diferencia en días es: {abs(diferencia_dias)} días.")

# Flujo del programa
clear_console()
fecha_usuario = input("Ingrese la fecha (dd/mm/yyyy): ")
calcular_diferencia(fecha_usuario)