# Ejercicio 10: Solicitar al usuario un numero n y calcular la suma de n + nn + nnn

# Ejemplo: 2
# suma = 2 + 22 + 222 = 246

from global_functions import clear_console 

# Manejo de excepciones para asegurar que el valor ingresado es un número positivo
try:
    clear_console()
    n = int(input("Ingrese el valor de n: "))
except ValueError:
    print("Error: Debes ingresar un número positivo.")
    clear_console()
    exit()

if n <= 0:
    print("Error: El valor ingresado debe ser un número positivo, mayor que cero.")
    clear_console()
    exit()
else:
    nn= int('{}{}'.format(n,n))
    nnn= int('%s%s%s' % (n,n,n))
    n= int(n)
    suma= n + nn + nnn

    print("La suma es:", suma)
    print()

# Fin de programa




 
 