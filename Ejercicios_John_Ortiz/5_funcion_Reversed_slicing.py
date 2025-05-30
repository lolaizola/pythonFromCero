# Ejercicio 5: Obtener la representación inversa de una cadena


# Ejemplo: Python ==> nohtyP

import time
import os
from global_functions import clear_console

# Manejo de excepciones para validar que la cadena no esté vacía
try:
    clear_console()
    cadena = str(input("Ingrese una cadena: "))
    if cadena == "":
        raise ValueError("La cadena no puede estar vacía.")
except ValueError as e:
    print(e)
    clear_console()
    exit()

# Uso del ciclo for para recorrer la cadena al revés
cadena_inversa = ""
for i in range(len(cadena) - 1, -1, -1):
    cadena_inversa += cadena[i]

print("La cadena invertida es:", cadena_inversa)
print()

# Obtener la cadena invertida usando el operador de rebanado (slicing)
# El operador de rebanado [::-1] invierte la cadena
# cadena[start:end:step], donde step es -1 para invertir
# cadena[start:end:step] es una forma de acceder a los elementos de una secuencia

print("La cadena inversa es:", cadena[::-1])

# Obtener la cadena invertida con la funcion reversed()
cadena_inversa_reversed = ''.join(reversed(cadena))
print("La cadena invertida usando reversed() es:", cadena_inversa_reversed)
print()
print("Fin de programa")
print()
# Fin de programa
