# Los kwargs

# es un parametor que empaqueta todos los argumentos en un diccionario

def hola(**kwargs):
    #print('Hola ' + kwargs['nombre'] + ' ' + kwargs['apellido'] + ' ' + kwargs['segundo_nombre'])
    print('Hola', end=' ')
    for clave, valor in kwargs.items():
        print(valor, end=' ') 
    
hola(titulo='Joven, ', nombre='Misael', apellido='Barbosa', ejem1=', estas', ejem2='aprendiendo', segundo_nombre='Python')