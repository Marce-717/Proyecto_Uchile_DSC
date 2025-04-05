# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 10:42:26 2025

@author: marce
"""

"""


Clase aprendiendo phyton 3
fecha: 04-04-2025
Autor: Marcelo Toro M.

"""

print("Esta es la primera clase de Phyton - Facultad Universidad de Chile")
print("")
print("Algunos requisitos para comenzar el curso:")
print("1) Abrir una cuenta en Gmail \n" + 
      "2) Abrir un cuenta en en entorno de trabajo en Github \n"  
      "3) Si trabajan encomputar personal se recomienda bajar en entorno de dasarrollo de Anaconda ")

"""
La primeros pasos son conocer los principales fuentes de información:
    
    
1) literatuda oficial del sitio web
    # https://docs.python.org/3/tutorial/index.html
    # https://github.com/mouredev/Hello-Python

2) Conocer algunas consideraciones del editor tales como: 
    a) Uso de almohadillas para comentar código (comillas simples, comillas dobles)
    b) Entender la funciones o constructos embebidos en Phyton (type(), print())

"""
print("Los primeros pasos será conocer como trabajar con un editor de datos")

# Uso de la función print()
print("Hola Mundo") # Cuando quiero imprimir por pantalla la palabra "Hola Mundo"
print("este es un alamcenamiento en número: ", 5) # Cuando quiero imprimir por panatalla numero 5 , int()
print("Marcelo Toro Miranda"+ "Ingeniero Agronomo Enologo"+ "Numero de registro 648") # Concatenar salidas de print() en forma de lista
print("Marcelo Toro Miranda", "Ingeniero Agronomo Enologo", "Numero de registro 648")
print("Marcelo", "-----------------", "me gusta programar")
print("")
print("Marcelo", "-----------------", "Este es un texto despues del espacio")
print("")

# Tipo de almacenamiento de datos
cadena_texto = "Este es una cadena de texto considerado como stream"
print("Este es considerado una cadena de texto stream: \n" + cadena_texto)

objeto_numero_float = 5.0
print("Este en un numero considerado como float: ", objeto_numero_float)

objeto_numero_int = 5
print("Este en un numero considerado como int: ", objeto_numero_int)

#################################### Conociendo las variables ###################################################
print("")
print("Conocer el tipo de datos que entrega el metodo Type()")
# Cómo consultar el tipo de dato
print(type("Soy un dato str"))  # Tipo 'str'
print(type(5))  # Tipo 'int'
print(type(1.5))  # Tipo 'float'
print(type(3 + 1j))  # Tipo 'complex'
print(type(True))  # Tipo 'bool'
print(type(print("Mi cadena de texto")))  # Tipo 'NoneType'

############################### Función input()#############################
print("Vamos a conocer la función imput()")
print("")
# Inputs
# nombre = input('¿Cuál es tu nombre? ')
# edad = input('¿Cuántos años tienes? ')
# print("El nombre que ingresó al sistema es", nombre, "y tiene la edad de ", edad, "años")


# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address)) 

################### Cambio de variables #######################

numero_int = 6
cambio_numero = str(numero_int)
print("En este caso cambiamos el tipo denumero int a stream",type(cambio_numero))

###################
print("")
print("Estamos utilizando la edito para realizar operaciones matematicas simples:\n")
print("Esta es la multiplicación de dos numero naturales", 5 * 5)
print("esta es la división de dos numeros naturales" , 5 / 5)
print("Esta es la suma de dos múmeros", 5 + 5)
print("esta es la resta de dos números", 5 - 3)
print("Esta es la división de dos numeros aproximados el piso: ", 7//3)

########################### Operaciones matematicas########################

print("Ejercicio de sacar el área de un rectángulo")
# Ejecutamos el ejercircio de sacar el área de un rectangulo

base = 8
altura = 7
area_cuadrado = base * altura
print("El área del traingulo es: ", area_cuadrado) 