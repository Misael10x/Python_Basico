## String cadena de caracteres

#nombre = "Misael"
#apellido = "Barbosa"
#nombreCompleto =  "Hola " + nombre + " " + apellido
#print(nombre) ## va sin comillas simples ni dobles ya que en este caso solo queremos mostrar lo que hay.
#print("Hola " + nombre)
#print(type(nombre)) #imprime el tipo de dato de la variable
#print(nombreCompleto)

## INT numero de dato entero

#edad = 22 # un dato entero no debe ir entre comillas ya que no es una cadena
#edad = edad + 1 (forma 1)
#edad += 1 # forma abreviada
#print(type(edad)) # saber el tipo de dato de la edad
#print("tu edad es: " + str(edad)) # convertimos nuestra variable edad en una cadena de caracteres con str

## FLOAT numero de dato decimal

# altura  = 180.5 # el decimal nos indica que es un numero flotante
# print(altura)
# print(type(altura)) # tipo de dato
# print("Tu altura es: " + str (altura)) # imprimir la altura dentro de una cadena de caracteres

## BOOL almacena dos valores verdadero o falso

humano = False
# print(humano)
# print(type(humano))
print("tu eres un humano: " + str (humano))