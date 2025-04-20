# Ejercicio 13:
import time
from global_functions import clear_console

# Ejemplo: usar ""para crear una cadena de texto multilínea.""
#          usar """ para crear una cadena de texto multilínea."""
#          usar '' para crear una cadena de texto multilínea.''
#          usar ''' para crear una cadena de texto multilínea.'''
#          usar \n para crear una cadena de texto multilínea.\n
#          usar \t para crear una cadena de texto multilínea.\t
#          usar \ para crear una cadena de texto multilínea.\
#          usar \r para crear una cadena de texto multilínea.\r
#          usar \b para crear una cadena de texto multilínea.\b
#          usar \f para crear una cadena de texto multilínea.\f
#          usar \v para crear una cadena de texto multilínea.\v
#          usar \a para crear una cadena de texto multilínea.\a
#          usar \x para crear una cadena de texto multilínea.\x
#          usar \u para crear una cadena de texto multilínea.\u


clear_console()

cadena = """Phyton es un lenguaje de programación interpretado, de alto nivel y de propósito general. Su diseño enfatiza la legibilidad del código y su sintaxis permite a los programadores expresar conceptos en menos líneas de código de lo que se requiere en otros lenguajes de programación, como C++ o Java."""

print(cadena)
print()

cadena = "Phyton es un lenguaje de programación interpretado, de alto nivel y de propósito general. Su diseño enfatiza la legibilidad del código y su sintaxis permite a los programadores expresar conceptos en menos líneas de código de lo que se requiere en otros lenguajes de programación, como C++ o Java."

print(cadena)
print()
cadena = '''Phyton es un lenguaje de programación interpretado, de alto nivel y de propósito general. Su diseño enfatiza la legibilidad del código y su sintaxis permite a los programadores expresar conceptos en menos líneas de código de lo que se requiere en otros lenguajes de programación, como C++ o Java.'''
print(cadena)
print()

cadena = 'Phyton es un lenguaje de programación interpretado, de alto nivel y de propósito general. Su diseño enfatiza la legibilidad del código y su sintaxis permite a los programadores expresar conceptos en menos líneas de código de lo que se requiere en otros lenguajes de programación, como C++ o Java.'
print(cadena)
print()

time.sleep(5)
print()

print("Fin de programa")
print()
# Fin de programa