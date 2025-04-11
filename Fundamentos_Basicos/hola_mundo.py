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
#Funcion bool para convertir un dato a booleano
#Funcion list para convertir un dato a lista
#Funcion tuple para convertir un dato a tupla
#Funcion set para convertir un dato a conjunto
#Funcion dict para convertir un dato a diccionario
#Funcion complex para convertir un dato a complejo
#Funcion bin para convertir un dato a binario
#Funcion hex para convertir un dato a hexadecimal
#Funcion oct para convertir un dato a octal
#Funcion chr para convertir un dato a caracter
#Funcion ord para convertir un dato a codigo ascii
#Funcion eval para evaluar una expresion
