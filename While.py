## Bucles while#
# Ejercicio: Hacer un programa que solicite al usuario que ingrese su nombre y si no lo ingresa pedirle que ingrese algo

# Ejemplo
# while 1 == 1:
# print("Ayuda estoy atrapado en un bucle")

# EJERCICIO 

nombre = ""

# Forma 1
#while len(nombre) == 0: # len es la longitud de la cadena
    #nombre = input("Ingresa tu nombre:" )

# Forma 2    
# print(not nombre) 

while not nombre or len(nombre) == 0:
    nombre = input("Ingresa tu nombre: ")
print("Hola " + nombre)
 