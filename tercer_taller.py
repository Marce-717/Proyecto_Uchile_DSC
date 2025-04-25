# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 10:47:22 2025

@author: marce
"""
"""
Taller de programación Phyton 3
viernes: 25-04-2025


Que vamos a ver hoy:
    1) Como manejar string y números dentro de ka función print()
    2) Funciones del lenguaje (capitalize(), upper(), lower(), count())
    3) 




"""
import os 

# Cambio de directorio

ruta_nueva = 'C:/Users/marce/OneDrive/Documentos/OneDrive/Documentos/Agricultura_digital/programación'  # Especifica la ruta deseada aquí
os.chdir(ruta_nueva)  # Cambia el directorio de trabajo
nueva_ruta = os.getcwd()  # Obtiene la ruta actual para verificar el cambio
print(nueva_ruta)  # Imprime la nueva ruta


print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote


##############################################################
print("")

print("Otra forma de empaquetar datos: \n")


# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  y números
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

# Como utilizar la funciión print() con insertar listas
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"
print("")

################### FUNCIONES DEL LENGUAJE ###########################################################
print("Funciones del lenguaje: \n")

language = "phyton"

# Funciones del lenguaje

print(language.capitalize()) # Coloca la primera letra en mayúscula
print(language.upper()) # todas las letras en mayúscula
print(language.count("t")) # cuenta el número de letras "t" de la cadena de texto
print(language.isnumeric()) # pregunta si es numerica
print("1".isnumeric()) # pregunta si es numerica
print(language.lower()) # coloca todas las letras en minúsculas
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo

#################### MÉTODOS DE STRINGS ####################################################


web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

print("")


challenge = 'thirty days of pythoonnn' 
print(challenge.strip('noth')) # 'irty days of py'

challenge = 'thirty days of python'
print(challenge.replace('of', 'and')) # 'thirty days of coding'

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON


################################ LISTAS ############################################

lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types
print(lst[1:3])
print("")
print("Slice através de la cedena de texto:")
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango

#################### EMPAQUETADO ###############################################

lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']


# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
print("")

print("desempacar una lista: ")
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
