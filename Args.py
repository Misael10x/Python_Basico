# Args
 
# es un parametro que empaqueta todos los argumentos en una tupla
# las tuplas no pueden ser modificadas

def suma(*args):
    suma = 0
    cosas = list(args)
    cosas[1] = 0
    for i in cosas:
        suma += i
    return suma
            

print(suma(1, 5, 3, 2, 7, 1))
    

