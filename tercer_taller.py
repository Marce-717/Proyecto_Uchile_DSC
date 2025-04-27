# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 10:47:22 2025

@author: marce
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 10:47:22 2025

@author: marce
"""

"""
Taller de programación Python 3
viernes: 25-04-2025

Que vamos a ver hoy:
    1) Como manejar string y números dentro de la función print()
    2) Funciones del lenguaje (capitalize(), upper(), lower(), count())
"""

import os  # Librería para interactuar con el sistema operativo

# Cambio de directorio
ruta_nueva = 'C:/Users/marce/OneDrive/Documentos/OneDrive/Documentos/Agricultura_digital/programación'  # Especifica la ruta deseada
os.chdir(ruta_nueva)  # Cambia el directorio de trabajo
nueva_ruta = os.getcwd()  # Obtiene la ruta actual para verificar el cambio
print(nueva_ruta)  # Imprime la nueva ruta actual

# Ejemplos de uso de print()
print('I hope everyone is enjoying the Python Challenge.\nAre you ?')  # \n crea un salto de línea
print('Days\tTopics\tExercises')  # \t añade un tabulador o 4 espacios
print('Day 1\t5\t5')  # Imprime información tabulada
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash symbol (\\)')  # Para escribir una barra invertida
print('In every programming language it starts with \"Hello, World!\"')  # Escribe una comilla doble dentro de un string

print("")  # Imprime una línea vacía

print("Otra forma de empaquetar datos: \n")  # Ejemplo de empaquetar strings y números usando print()

# Strings only
first_name = 'Asabeneh'  # Nombre
last_name = 'Yetayeh'  # Apellido
language = 'Python'  # Lenguaje
formated_string = 'I am %s %s. I teach %s' % (first_name, last_name, language)  # Formatea la cadena de texto
print(formated_string)  # Imprime la cadena formateada

# Strings y números
radius = 10  # Radio
pi = 3.14  # Valor de pi
area = pi * radius ** 2  # Calcula el área de un círculo
formated_string = 'The area of circle with a radius %d is %.2f.' % (radius, area)  # Formatea el string con un número y un float
print(formated_string)  # Imprime el resultado formateado

# Como utilizar la función print() para insertar listas
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']  # Lista de librerías de Python
formated_string = 'The following are python libraries:%s' % (python_libraries)  # Formatea una lista dentro de un string
print(formated_string)  # Imprime la lista formateada como string

print("")  # Línea vacía

################### FUNCIONES DEL LENGUAJE ###########################################################
print("Funciones del lenguaje: \n")  # Imprime una introducción a funciones del lenguaje

language = "phyton"  # String de ejemplo

# Funciones del lenguaje
print(language.capitalize())  # Coloca la primera letra en mayúscula
print(language.upper())  # Convierte todo el texto a mayúsculas
print(language.count("t"))  # Cuenta el número de ocurrencias de la letra "t"
print(language.isnumeric())  # Verifica si el string es numérico
print("1".isnumeric())  # Verifica si el string "1" es numérico
print(language.lower())  # Convierte todo el texto a minúsculas
print(language.lower().isupper())  # Verifica si el string en minúsculas está en mayúsculas (devolverá False)
print(language.startswith("Py"))  # Verifica si el string comienza con "Py" (False, porque es "phyton")
print("Py" == "py")  # Compara si "Py" es igual a "py" (False)

#################### MÉTODOS DE STRINGS ####################################################

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']  # Lista de tecnologías web
result = ' '.join(web_tech)  # Une los elementos de la lista separados por un espacio
print(result)  # Imprime el resultado como un string unido

print("")  # Línea vacía

challenge = 'thirty days of pythoonnn'  # String de ejemplo
print(challenge.strip('noth'))  # Elimina los caracteres 'n', 'o', 't', 'h' desde los extremos del string

challenge = 'thirty days of python'  # String de ejemplo
print(challenge.replace('of', 'and'))  # Reemplaza 'of' con 'and'

challenge = 'thirty days of python'  # String de ejemplo
print(challenge.split())  # Divide el string en una lista por espacios
challenge = 'thirty, days, of, python'  # String con comas
print(challenge.split(', '))  # Divide el string en una lista por comas y espacios

challenge = 'thirty days of python'  # String de ejemplo
print(challenge.swapcase())  # Cambia mayúsculas por minúsculas y viceversa
challenge = 'Thirty Days Of Python'  # Otro string
print(challenge.swapcase())  # Cambia mayúsculas por minúsculas y viceversa

################################ LISTAS ############################################

lst = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]  # Lista con diferentes tipos de datos
print(lst[1:3])  # Imprime un slice de la lista (índices 1 y 2)
print("")  # Línea vacía

print("Slice através de la cadena de texto:")  # Introducción a operaciones con listas
fruits = ['banana', 'orange', 'mango', 'lemon']  # Lista de frutas
first_fruit = fruits[-4]  # Primer elemento usando índice negativo
last_fruit = fruits[-1]  # Último elemento
second_last = fruits[-2]  # Penúltimo elemento
print(first_fruit)  # Imprime 'banana'
print(last_fruit)  # Imprime 'lemon'
print(second_last)  # Imprime 'mango'

#################### EMPAQUETADO ###############################################

lst = ['item1', 'item2', 'item3', 'item4', 'item5']  # Lista de ejemplo
first_item, second_item, third_item, *rest = lst  # Desempaqueta los primeros 3 elementos y guarda el resto
print(first_item)  # Imprime 'item1'
print(second_item)  # Imprime 'item2'
print(third_item)  # Imprime 'item3'
print(rest)  # Imprime ['item4', 'item5']

# Ejemplo 1 de desempacar listas
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']  # Lista de frutas
first_fruit, second_fruit, third_fruit, *rest = fruits  # Desempaqueta los primeros 3 elementos y guarda el resto
print(first_fruit)  # Imprime 'banana'
print(second_fruit)  # Imprime 'orange'
print(third_fruit)  # Imprime 'mango'
print(rest)  # Imprime ['lemon', 'lime', 'apple']

# Ejemplo 2 de desempacar listas
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de números
print(first)  # Imprime 1
print(second)  # Imprime 2
print(third)  # Imprime 3
print(rest)  # Imprime [4, 5, 6, 7, 8, 9]
print(tenth)  # Imprime 10
print("")  # Línea vacía

print("desempacar una lista: ")  # Introducción al tema
# Ejemplo 3 de desempacar listas
countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']  # Lista de países
gr, fr, bg, sw, *scandic, es = countries  # Desempaqueta los primeros 4 elementos, agrupa el resto excepto el último
print(gr)  # Imprime 'Germany'
print(fr)  # Imprime 'France'
print(bg)  # Imprime 'Belgium'
print(sw)  # Imprime 'Sweden'
print(scandic)  # Imprime ['Denmark', 'Finland', 'Norway', 'Iceland']
print(es)  # Imprime 'Estonia'