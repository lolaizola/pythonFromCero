# Que es una variable?
# Una variable es un espacio en memoria que almacena un valor, el cual puede cambiar a lo largo del tiempo.

# Que es una funcion?
# Una funcion es un bloque de codigo que se puede reutilizar, el cual tiene un nombre y puede recibir parametros.
# Una funcion puede devolver un valor o no devolver nada.
# Una funcion puede recibir parametros o no recibir nada.
# Una funcion puede ser llamada varias veces en el mismo programa.
# Una funcion puede ser llamada desde otra funcion.
# Una funcion puede ser llamada desde cualquier parte del programa.

# Estructura de una funcion
# 1. Nombre: nombre_funcion(parametros)
# 2. Parametros: nombre_funcion: nombre de la funcion, parametros: variables que recibe la funcion
# 3. Resultado de una funcion: nombre_funcion(parametros)    

# Funcion Print para imprimir en pantalla

#Uso de variables
name="Luis Alfredo"
Edad= 52
Estatura= 1.71

print("Hola ", name, " ¿Cómo estás?")
print("Bienvenido al curso de Python")

#Funcion type para saber el tipo de dato de una variable

print("==== Seccion uso de funcion 'type' ====")
print("El tipo de dato de la variable name es: ", type(name))
print("El tipo de dato de la variable Edad es: ", type(Edad))
print("El tipo de dato de la variable Estatura es: ", type(Estatura))

#Funcion int para convertir un dato a entero
#Ejemplo: int("10") = 10
print("==== Seccion uso de funcion 'int' ====")
resultado= "10"
print("El tipo de dato de la variable resultado es: ", type(resultado))
resultado= int(resultado)
print("El resultado de la conversion es: ", type(resultado))

#Funcion float para convertir un dato a decimal
#Ejemplo: float("10.5") = 10.5
print("==== Seccion uso de funcion 'float' ====")
resultado= "10.5"
print("El tipo de dato de la variable resultado es: ", type(resultado))
resultado= float(resultado)
print("El resultado de la conversion es: ", type(resultado))

#Funcion str para convertir un dato a cadena de texto
#Ejemplo: str(10) = "10"
print("==== Seccion uso de funcion 'str' ====")
resultado= 10
print("El tipo de dato de la variable resultado es: ", type(resultado))
resultado= str(resultado)
print("El resultado de la conversion es: ", type(resultado))

#Funcion bool para convertir un dato a booleano
#Ejemplo: bool(1) = True, bool(0) = False
print("==== Seccion uso de funcion 'bool' ====")
resultado= 1
print("El tipo de dato de la variable resultado es: ", type(resultado))
resultado= bool(resultado)
print("El resultado de la conversion es: ", type(resultado))

#Funcion list para convertir un dato a lista
#Ejemplo: list("Hola") = ["H", "o", "l", "a"]
print("==== Seccion uso de funcion 'list' ====")
resultado= "Hola"
print("El tipo de dato de la variable resultado es: ", type(resultado))
resultado= list(resultado)
print("El resultado de la conversion es: ", type(resultado))

#Funcion tuple para convertir un dato a tupla
#Ejemplo: tuple("Hola") = ("H", "o", "l", "a")
print("==== Seccion uso de funcion 'tuple' ====")
resultado= "Hola"
print("El tipo de dato de la variable resultado es: ", type(resultado))
resultado= tuple(resultado)
print("El resultado de la conversion es: ", type(resultado))

#Funcion set para convertir un dato a conjunto
#Ejemplo: set("Hola") = {"H", "o", "l", "a"}
print("==== Seccion uso de funcion 'set' ====")
resultado= "Hola"
print("El tipo de dato de la variable resultado es: ", type(resultado))
resultado= set(resultado)
print("El resultado de la conversion es: ", type(resultado))

#Funcion dict para convertir un dato a diccionario
#Ejemplo: dict(a=1, b=2) = {"a": 1, "b": 2}
print("==== Seccion uso de funcion 'dict' ====")
resultado= {"a": 1, "b": 2}
print("El tipo de dato de la variable resultado es: ", type(resultado))
resultado= dict(a=1, b=2)
print("El resultado de la conversion es: ", type(resultado))

#Funcion complex para convertir un dato a complejo
#Ejemplo: complex(1, 2) = 1 + 2j
print("==== Seccion uso de funcion 'complex' ====")
resultado= 1 + 2j
print("El tipo de dato de la variable resultado es: ", type(resultado))
resultado= complex(1, 2)
print("El resultado de la conversion es: ", type(resultado))

#Funcion bin para convertir un dato a binario
#Ejemplo: bin(10) = 0b1010
print("==== Seccion uso de funcion 'bin' ====")
resultado= 10
print("El tipo de dato de la variable resultado es: ", type(resultado))
resultado= bin(resultado)
print("El resultado de la conversion es: ", type(resultado))

#Funcion hex para convertir un dato a hexadecimal
#Ejemplo: hex(10) = 0xa
print("==== Seccion uso de funcion 'hex' ====")
resultado= 10
print("El tipo de dato de la variable resultado es: ", type(resultado))
resultado= hex(resultado)
print("El resultado de la conversion es: ", type(resultado))

#Funcion oct para convertir un dato a octal
#Ejemplo: oct(10) = 0o12
print("==== Seccion uso de funcion 'oct' ====")
resultado= 10
print("El tipo de dato de la variable resultado es: ", type(resultado))
resultado= oct(resultado)
print("El resultado de la conversion es: ", type(resultado))

#Funcion chr para convertir un dato a caracter
#Ejemplo: chr(65) = "A"
print("==== Seccion uso de funcion 'chr' ====")
resultado= 65
print("El tipo de dato de la variable resultado es: ", type(resultado))
resultado= chr(resultado)
print("El resultado de la conversion es: ", type(resultado))

#Funcion ord para convertir un dato a codigo ascii
#Ejemplo: ord("A") = 65
print("==== Seccion uso de funcion 'ord' ====")
resultado= "A"
print("El tipo de dato de la variable resultado es: ", type(resultado))
resultado= ord(resultado)
print("El resultado de la conversion es: ", type(resultado))

#Funcion eval para evaluar una expresion
#Ejemplo: eval("10 + 5") = 15
print("==== Seccion uso de funcion 'eval' ====")
resultado= "10 + 5"
print("El tipo de dato de la variable resultado es: ", type(resultado))