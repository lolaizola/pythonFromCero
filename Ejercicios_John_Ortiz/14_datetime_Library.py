# Ejercicio 14: Calcular la diferencia en dias entre dos fechas obtenidas por pantalla.

import time
from datetime import datetime
from global_functions import clear_console, validar_fecha


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
#validar_fecha(fecha_usuario)
calcular_diferencia(fecha_usuario)
print()
print("Fin de programa")
print()

# Fin de programa