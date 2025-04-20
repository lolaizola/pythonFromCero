# Ejercicio 8: Obtener el primer y ultimo elemento de una lista

# Ejemplo: lenguajes = ['Python', 'Java', 'C++', 'JavaScript']

# limpiar la consola
import os
import time
from typing import List
from typing import Tuple
from global_functions import clear_console


# Manejo de excepciones para validar que la lista no esté vacía y sea una lista válida
try:
    clear_console()
    lista = str(input("Ingrese una lista de elementos separados por comas: "))
    if not lista.strip():
            raise ValueError("La lista no puede estar vacía.")
    elif ',' not in lista:
            raise ValueError("La lista debe contener 2 elementos como minimo")
    elif lista.split(",")[-1] == "":
            raise ValueError("El ultimo elemento de la lista no puede estar vacío.")
except ValueError as e:
    print(e)
    clear_console()
    exit()

# Obtener el primer y último elemento de la lista
primer_elemento = lista[0]
ultimo_elemento = lista[-1]
print("El primer elemento de la lista es:", primer_elemento)
print("El último elemento de la lista es:", ultimo_elemento)
print()

# Funcion length para contar el número de elementos en la lista
primer_elemento = lista[0]
ultimo_elemento = lista[len(lista)-1]
print("El primer elemento de la lista es:", primer_elemento)
print("El último elemento de la lista es:", ultimo_elemento)
print()

def obtener_primer_y_ultimo_elemento(lista: str) -> Tuple[str, str]:
    elementos = lista.split(",")
    primer_elemento = elementos[0].strip()
    ultimo_elemento = elementos[-1].strip()
    return primer_elemento, ultimo_elemento
print("El primer y último elemento de la lista son:")
print(obtener_primer_y_ultimo_elemento(lista))
print()

print("Fin de programa")
print()
# Fin de programa