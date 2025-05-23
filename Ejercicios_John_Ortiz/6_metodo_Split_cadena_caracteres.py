# Ejercicio 6: Obtener un conjunto de numeros separados por coma y crear una lista usando el metodo split

# Ejemplo: 1,2,3,4,5 ==> [1, 2, 3, 4, 5]

import time
import os
from typing import List
from global_functions import clear_console

# Manejo de excepciones para validar que la cadena no esté vacía y sean numeros positivo

try:
    clear_console()
    cadena = str(input("Ingrese una cadena de números separados por coma: "))
    if not all(part.strip().isdigit() for part in cadena.split(",")):
        raise ValueError("La cadena debe contener solo números separados por comas.")
    if cadena == "":
        raise ValueError("La cadena no puede estar vacía.")
except ValueError as e:
    print(e)
    clear_console()
    exit()

# Uso del metodo strip() para eliminar espacios en blanco y el metodo split() para separar la cadena por comas
numeros: List[int] = [int(num.strip()) for num in cadena.split(",")]
print("La lista de números es:", numeros)
print(type(numeros))
print()

# Obtener la lista de números usando el método split() y la función map()
numeros_map: List[int] = list(map(int, cadena.split(",")))
print("La lista de números usando map() es:", numeros_map)
print(type(numeros_map))
print()

# Obtener la lista de números usando el método split() y la función filter()
numeros_filter: List[int] = list(filter(lambda x: x.isdigit(), cadena.split(",")))
print("La lista de números usando filter() es:", numeros_filter)
print(type(numeros_filter))
print()

# Obtener la lista de números usando el método split() y la función list comprehension
numeros= cadena.split(",")
print("La lista de numeros usando split es:", numeros)
print(type(numeros))
print()

print("Fin de programa")
print()
# Fin de programa