# Ambito de las variables

# una variable solo esta disponible desde dentro de la region en la que se crea
# las variables locales solo estan disponibles para la funcion donde se crea
# las variables globales se declara fuera de cualquier funcion pero dentro del modulo  en el que se trabaja
# regla LEGB (variables locales, variables cercanas, variables globales y variables integradas)


nombre = 'Barbosa' # variable global

def mostrar_nombre(): 
    #nombre = 'Misael' # variable local
    print(nombre)
    
mostrar_nombre();
#print(nombre)
    