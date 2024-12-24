# reduce (Funcion, iterable)

import functools

letras = ["H", "O", "L", "A"]

palabra = functools.reduce(lambda x,y: x+y, letras)

print(palabra)
