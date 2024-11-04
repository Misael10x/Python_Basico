# Diccionarios 

# es una coleccion modificable y no ordenada de clave unico valor

capitales = {
    'EE.UU': 'Washiton D.C',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago de Chile',
    'Brasil': 'Brasilia',
    'cursos': ['Python', 'C++'],
    'año': 22
}
#capitales.update({'Àlemania': 'Berling'})
#capitales.pop('EE.UU')
#capitales.clear()

#print(capitales.get('Argentina'))  es para saber si existe la clave
#print(capitales.keys()) es para ver las claves del diccionario
#print(capitales.values()) es para traer los valores que almacena el diccionario
#print(capitales.items()) traer las llaves como los valores
for key, value in capitales.items():# Forma dos de traer todos los valores
    print(key,value)
