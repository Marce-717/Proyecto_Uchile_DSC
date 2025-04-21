# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 16:35:24 2025

@author: marce
"""

"""
TALLER DE PROGRAMACIÓN PHYTON
Autor: Marcelo Toro M
Fecha: jueves 11 de abril 2025

"""

"""

¿Que vimos la primera clase?
    1) Como asignar una variable como str(), int(), float().
    2) Vimos funciones embebidas de Phtyon tales como print(), type(), int() y str().
    3) 

¿Que vamos a ver hoy?
    1) Editor como calculadora, 4 operaciones básicas.
    2) operadores comparativos, asignación 
    3) elementos "and" y "or"

"""

import os 

# Cambio de directorio

ruta_nueva = 'C:/Users/marce/OneDrive/Documentos/OneDrive/Documentos/Agricultura_digital/programación'  # Especifica la ruta deseada aquí
os.chdir(ruta_nueva)  # Cambia el directorio de trabajo
nueva_ruta = os.getcwd()  # Obtiene la ruta actual para verificar el cambio
print(nueva_ruta)  # Imprime la nueva ruta

# Operaciones con enteros

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))

######################### OPERADORES COMPARATIVOS #########################


print("")
print("Operadores Comparativos con números: \n")
# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)
print("")
# Operaciones con cadenas de texto
# Phyton cuentas los string como número de caracteres
print("Operadores comparativos con string: \n")
print("Hola" > "Python") 
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")
print("")
# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print("Operadores de "and" y "or" también llamado booleano: \n")
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))


################## CADENAS DE TEXTO (STRING)  ################################################

print("")
### Cadenas de texto ###
print("Como unir cadenas de texto con operadores de +")
cadena_texto = "Esto es una cadena de texto"
otra_cadena_texto = 'Esta es otra cadena de texo para explicar'

print(len(cadena_texto))
print(len(otra_cadena_texto))
print(cadena_texto + " " + otra_cadena_texto)

print("")
cadena_salto_linea = "Este es una cadena de texto\ncon salto de línea"
print(cadena_salto_linea)

cadena_tabulacion = "\tEste es una cadena con tabulación"
print(cadena_tabulacion)
print("")


# Formateo

nombre, apellido, edad = "Marcelo", "Toro", 82
print("Mi nombre es {} {} y mi edad es {}".format(nombre, apellido, edad))
print("Mi nombre es %s %s y mi edad es %d" % (nombre, apellido, edad))
print("Mi nombre es " + nombre + " " + apellido + " y mi edad es " + str(edad))
print(f"Mi nombre es {nombre} {apellido} y mi edad es {edad}")
print("")
# Desempaqueado de caracteres
print("Empaquetar caracteres:")
language = "python"
a, b, c, d, e, f = language 
print(a)
print(e)
print("")
# División
print("Como me deslizo através de una cadena de texto")
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)
print("")
# Reverse
print("Función de reverse")
reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje
print("Funciones del lenguaje")
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo 