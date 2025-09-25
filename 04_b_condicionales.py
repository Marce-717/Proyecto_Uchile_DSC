# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 18:18:32 2025

@author: marce
"""

"""

Autor: Marcelo Toro Miranda
Fecha: 27 agosto 2025

temas a tratar:
    - Recordatorio de prueba 4 de septiembre: lógica de programación, estructura de datos, ciclos iterativos y funciones
    - Hoy hay control N°2
    - Preguntas


Temas que veremos hoy: - Funciones
                       - Condicionales (if, else, elif)
                       - Bucles (while, for) 
                       
"""

#################### FUNCIONES ###################################


def funcion():
    print("esta es una función")

def funcion():
    return  funcion  
 
# funcion()
# funcion()
# funcion()

# Definir una función con parametros y argumentos

def suma(primer_parametro, segundo_parametro):
    print(primer_parametro + segundo_parametro)
    
suma(8, 8)
suma(5, 5)
suma(2.0,2)

def otra_suma(primer_parametro, segundo_parametro):
    return primer_parametro + segundo_parametro

print("Esta es la forma correcta de definir una función: ", otra_suma(5,5))

def otra_suma(primer_parametro, segundo_parametro):
    suma = primer_parametro + segundo_parametro
    return suma

def resta(parametro_uno, parametro_dos):
    diferencia = (parametro_uno - parametro_dos) / 4
    expon = diferencia * 2**3
    return expon

print("Esta es un retorno de la funicón exponente", resta(4, 2))

#Llamado de funicion otra suma
print("esta es una función de concatenion de string y no de la funion de suma de numeros \n",
      otra_suma("4","5"))

# Otra funcion con ingresos de parametros definidos previamente

def sumatoria(primer_numero: int, segundo_numero: int):
    return primer_numero + segundo_numero

print(sumatoria(4.4, 5.0))


# Revisaeremos la función con string

def nombres(nombre, apellido, alias= "ing agronomo"):
    return (f'{nombre} {apellido} {alias}')

# print(nombres("Marcelo","Toro"))
# print(nombres("Aurelio","Muñoz"))
print(nombres("Marcelo","Toro","agronomo"))
print(nombres("Marcelo","Toro"))

# funcion con parametros text

def print_upper_text(*text):
      for text in text:
          print(text.lower())

################### Condicionales ################################3
print("--------------------")
condicion = 5 * 3

if condicion <= 10:
    print("Esta condicion es menor o igual que 10")
    
if condicion == 15:
    print("Esta condicion es igual a 15")

if condicion >= 10:
    print("Esta condicion es mayor o igual que 10")
    
if condicion >= 10 and condicion >=20:
    print("este numero se encuentra entre 10 y 20")
    
# Segunada forma por defecto

segunda_condicion = 5 * 4

if segunda_condicion == 20:
    print("Esta segunda condicion se cumple da como rerusltado 20")
    
else:
    print("Esta condicion no se cumple")
    
######## ELIF ###############################


condicion = 5 * 100

if condicion <= 10:
    print("Esta condicion es menor o igual que 10")

elif condicion >= 10 and condicion <= 20:
    print("esta numero se encuentra enytre 10 y 20")

elif condicion >= 20 and condicion <= 40:
    print("esta numero se encuentra entre 20 y 40")
    
else:
    print("Esta condicion no cumple con ningunas de las condionces")
    
print("")  
print("Esta es una condicion final")

