# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 11:39:00 2025

@author: marce
"""
 
import pandas as pd
import numpy as np
import os
# from bs4 import BeautifulSoup
# import requests3
# from docx import Document
# from docx.shared import Pt

# Metodo para cambio de directorio con libreria os

ruta_nueva = 'C:/Users/marce/OneDrive/Documentos/OneDrive/Documentos/Data_Science_Renares/Compartido_DataScience_Uchile/Scripts clases'  # Especifica la ruta deseada aquí
os.chdir(ruta_nueva)  # Cambia el directorio de trabajo
nueva_ruta = os.getcwd()  # Obtiene la ruta actual para verificar el cambio
print(nueva_ruta)  # Imprime la nueva ruta

################################################################################

"""
I) Resultados del control
    - Espacio para consultas en miercoles 27 de agosto 11 a 13 hr
    - Criterio de evaluación
    - Evaluación a traves de test u-cursos el 4 de septiembre
    
Que vimos en clase anterior
    1) Manejo de la consola
    2) Asignación de variables numericas y strings
    3) Funciones incorporadas en phyton (type, int, str, len, round)

Que vamos a ver hoy:
    - Abrir usuario en Github   
    - Strings    
    - Estructuras de almacenamiento de datos (Listas, tuplas, set, diccionarios)

lista: - Es una forma de agrupar elementos o datos en un orden definido
        - como hacemos slicing dentro de una lista
        - constructores (append, insert, pop, clear, remove, del, copy, reverse)

Tuplas: Otra forma de agrupar elementos, los elementos no son modificables
        - Constructores (count, index), del
        - no son modificables
        - se pueden cambiar a lista (transfromar una tupla a lista para poder modificarla)
        
set: No es una estructura ordenada
    - Un set no admite repetidos
    - No asegura un orden
    - Posibilidad de consultar datos (in)
    - métodos (remove(), clear(), union(), difference())
    
Diccionarios: Estructura clave-valor
    - Se le pueden pasar otrso tipos de datos(listas, set) 
    - En paginas web son json
"""

print("-----------------")

################## LISTAS ############################################


"""
list()

Se define con corchetes: mi_lista = [1, 2, 3]

Puede contener cualquier tipo de dato, incluso otras listas.

Métodos útiles: .append(), .remove(), .sort(), .reverse(), pop().

"""

lista = list()
otra_lista = []

lista = ["agronomia", " forestal","forestal", "recursos", 35, 7]
otra_lista = ["Juan", "Pedro", 67, "jueves"]
tercera_lista = ["semana"]
print(lista)
# print("Verificar la longitud de la lista: ",len(lista))
print(otra_lista)

print("Este es el primer elemento de la lista",lista[0])
print("Este es el tercer elemento de la lista",lista[2])
print("Este es el cuarto elemento de la lista",lista[3])

# Operaciones que puedo hacer con las listas


lista_concatenada = lista + otra_lista + tercera_lista
print(lista_concatenada)
print("este es la invovcaion del ultimo elemnto ", lista[-4])
print("Quiero llamar varios elemntos de la lista: ", lista[0:3])
print(len(lista))

# Ingresar elemntos dentro de una lista por el metodo .append()
# Metodos = .append; insert(); .copy(); remove(); pop(); reverse()

nueva_lista = lista.append("Pedro")
nueva_lista

# otra forma insertar atraves un elemnto con el metodo .insert()
lista.insert(4, "Eusebio")
print(lista)

lista_2 = lista.copy()
print(lista_2)

# CAmbiar un elemnto de lista
lista = ["agronomia", "forestal","forestal", "recursos", 35, 7]
# otra_lista = ["Juan", "Pedro", 67, "jueves"]
# tercera_lista = ["semana"]

lista[0] = "medicina"
lista[3] = "Agronomia"
print(lista)

# quiero sacar un elemnto de la lista
lista.remove("medicina")
print(lista)

lista.remove(35)
print(lista)

# metodo pop()
# Borra el ultimo elmento del objeto lista

lista.pop(3)
print(lista)

# elimimnar todos los elementos de una lista

# lista.clear()
# print(lista)

# Quiero boirrar el objeto lista
# del lista
# print(lista)

# Reversar la lista de objeto
lista.reverse()
print(lista)

# Hacer sublistas vacia

truncada = lista[5:10]
print(truncada)

################# TUPLAS ###########################

"""

Se define con paréntesis: mi_tupla = (1, 2, 3)

Ideal para datos que no deben cambiar.

Más eficiente en memoria que una lista.

Puede usarse como clave en un dict si sus elementos también son inmutables.

"""

# Caracteristicas de una tupla 

mi_tupla = tuple()
# print("este es el objeto tupla: ",mi_tupla)
# print("este es el objeto tupla: ",type(mi_tupla))

mi_tupla = ("agronomia", "forestal","forestal","Recursos")
print(type(mi_tupla))
print(len(mi_tupla))

# Como acceder a los elemntos de la tupla (Slicing)

print(mi_tupla[0])
print(mi_tupla[1])
print(mi_tupla[-1])
print(mi_tupla[-2])

# Cambiar elemnto de la tupla
otra_tupla = mi_tupla.count("forestal")
print("metodo count permite conocer numero de elemntos de la tupla asiganada a froestal: ",otra_tupla)

# Cambiar de estructora de datos tupla a lista y viciversa con los metodos list() y tuple()
tupla_lista =list(mi_tupla)
print(type(tupla_lista))

obejto_nuevo_tupla = tuple(tupla_lista)
print(obejto_nuevo_tupla)

# del obejto_nuevo_tupla
# print(obejto_nuevo_tupla)

######################## SET ##################################

"""

Se define con llaves o con set(): mi_set = {1, 2, 3}

Elimina automáticamente duplicados.

Muy útil para operaciones como unión, intersección, diferencia.

Métodos útiles: .add(), .remove(), .union(), .intersection()

"""

mi_set = set()
print(type(mi_set))
print(len(mi_set))

mi_set = {"agronomia","forestal","recursos","veterinaria","agronomia", 54, 79}
print("Este es mi primer set de datos: \n", mi_set)
print("Este es mi primer set de datos: \n", type(mi_set))
print("Cantidad de elemnetos: \n", len(mi_set))

# insertar elementodentro de un set

mi_set.add("medicina")
print(mi_set)

mi_set.add("quimica")
print(mi_set)

# remover elemntos de mi set

# mi_set.remove("agronomia")
# mi_set.remove("forestal")
# print(mi_set)

# Metodo que sirve para borarar mi set .clear(); union()

# mi_set.clear()
# print(mi_set)

# Buscar elementos dentro de un set
print("Esta es la foramde buscar un elemnento dentro de un set \n","agronomia" in mi_set)

otro_set = {"Pedro","Jose","agronomia", "forestal","recursos","veterinaria"}
otro_set_datos = {4, 6, 7}
# Tranformar un set
set_hecho_lista = list(mi_set)
print(set_hecho_lista[4])

# print("Me arroja un error porque no puedo sumar dos set: ", mi_set + otro_set)

otro_objeto_set = mi_set.union(otro_set).union(otro_set_datos)
print(otro_objeto_set)

print(otro_set.difference(mi_set))

########### Diccionarios ##############################
"""

dict()

Se define con llaves: mi_dict = {'clave': 'valor'}

Las claves deben ser únicas e inmutables (strings, números, tuplas).

Métodos útiles: .keys(), .values(), .items(), .get()

"""

diccionario = dict()
otro_diccionario = {}

print(type(otro_diccionario))
print(len(otro_diccionario))

diccionario = {"uno": 30, 
               "dos": "agronomia", 
               3:"forestal", 
               "list":[1,2,3,4],
               "dicc": {"siete":7, "ocho":78}
               }
           
print(diccionario[3])                    
print(diccionario["dicc"])

# insertar elemntos del dicionario

# diccionario["uno"] = "jjjjjjjjjjjjjjjjjjjjj"
# print(diccionario)

# Buscar un elemnto dentro del diccionario. el resultado es un Tru o False

print("Buscar un elemnto si esta dentro de mi diccioonario: \n","agronomia" in diccionario)

# Métodos para recorrer un diciconario y conocer tu contenido de llaves y valores
print("Llamado de todos los llave- valor: ",diccionario.items())
print("")
print("llamado a todos los llaves",diccionario.keys())
print("")
print("Llamda a los valores ",diccionario.values())


diccionario["color"] = "verde"
# print(diccionario)
otro_dict = diccionario.copy()
print(otro_dict)



