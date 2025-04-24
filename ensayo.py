# syntax# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
print(st)

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
print(fruits)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
print(st1)
print("")
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
print(st2)
print(st1)


################## DICCIONARIOS #####################################

# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct)

print("Otra forma de hacer un diccionario \n")

person = {
    'Nombre':'Asabeneh',
    'Apellido':'Yetayeh',
    'edad':250,
    'pais':'Finland',
    'estado_civil':True,
    'Habilidades':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(person)
print("que tipo de datos es: ", type(person))
print("")
print("Para saber la longitud del diccionario se utiliza la función len(): \n", len(person))
print("Para acceder a los atributos se ingresa por el valo y la llave. \n", person['Nombre'])

print(person.get('Nombre')) # Asabeneh
print(person.get('Pais'))    # Finland
print(person.get('Habilidades')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))

person['calle'] = 'Santa Rosa'

person['estado_civil'] = 'Casado'

print(person)
print("")
print(person.items())