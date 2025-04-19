# Ejercicio # 4: Solicitar el valor del radio de un circulo para calcular su area.

# Importar la librería math para realizar cálculos matemáticos

from math import pi
from global_functions import clear_console



# Manejo de excepciones para asegurar que el valor ingresado es un número positivo
try:
    clear_console()
    radio = float(input("Ingrese el radio del circulo: "))
except ValueError:
    print("Error: Debes ingresar un número positivo.")
    clear_console()
    exit()

if radio <= 0:
    print("Error: El radio debe ser un número positivo o mayor que cero.")
    clear_console()
    exit()
else:
    area = pi * radio ** 2

    # Mostrar el resultado al usuario

    print("El área del círculo es:", area)
    print()
    print("El área del círculo es: {:.2f}".format(area))
