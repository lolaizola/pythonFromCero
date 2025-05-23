# Ejercicio 3: Obtener la fecha y hora actual del sistema.

import datetime
from global_functions import clear_console


# Limpiar la consola

clear_console()

now = datetime.datetime.now()
print("Fecha y hora actual:", now)

# Formateo de la fecha y hora

formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
print("Fecha y hora formateada:", formatted_date)
print()
print("Fecha:", now.date())
print("Hora:", now.time())
print("Año:", now.year)
print("Mes:", now.month)
print("Día:", now.day)
print("Hora:", now.hour)
print("Minuto:", now.minute)
print("Segundo:", now.second)
print("Microsegundo:", now.microsecond)
print("Día de la semana:", now.strftime("%A"))
print("Número de semana:", now.strftime("%U"))
print("Número de día del año:", now.strftime("%j"))
print("Número de semana del año:", now.strftime("%W"))
print("Número de día del mes:", now.strftime("%d"))
print("Número de mes:", now.strftime("%m"))
print("Número de año:", now.strftime("%Y"))
print("Número de hora:", now.strftime("%H"))
print("Número de minuto:", now.strftime("%M"))
print("Número de segundo:", now.strftime("%S"))
print("Número de microsegundo:", now.strftime("%f"))
print("Número de zona horaria:", now.strftime("%Z"))
print("Número de hora UTC:", now.strftime("%z"))
print("Número de hora local:", now.strftime("%z"))
print("Número de hora GMT:", now.strftime("%z"))

print("Fin de programa")
print()
# Fin de programa