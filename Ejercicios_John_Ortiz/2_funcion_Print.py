# Ejercicio 2: Exponer el uso basico de la funcion print.

# Obtener librerias

from global_functions import clear_console


# Limpiar la consola

clear_console()


# Ejemplo 1:

print('Este es un ejemplo de la funcion print')
print("Este es otro ejemplo de la funcion print")

print('''Este es un ejemplo de la funcion print
con tres comillas simples''')

print("""Este es un ejemplo de la funcion print
con tres comillas dobles""")

# Ejemplo 2: Argumentos de la funcion print

print('Hola', 'mundo', '!', end=' ')
print()
print('Hola', 'mundo', '!', sep='-', end='.\n')

# Ejemplo 3: Formateo de cadenas

print('{} es {}'.format('Python', 'genial'))

print('{0} es {1}'.format('Python', 'genial'))
print('{1} es {0}'.format('Python', 'genial'))

print("Fin de programa")
print()
# Fin de programa