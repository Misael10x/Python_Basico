## Manipular cadenas

nombre = "Misael Barbosa"
primer_nombre = nombre [0:6] # Siempre el primer valor sera 0 en este caso de la primera letra osea M
#NOTA: si colocamos de 0 a 5 nos sale misae lo cual solo cambiamos el indice de finalizacion a 6 ya que es excluyente#
apellido = nombre [7:14]
nombre2 = nombre [0:14:4] #la tercera ilera son los saltos que hace en la cadena
nombre_invertido = nombre [::-1] # la cadena en orden invertido
website = "http://www.wikipedia.com"

slice= slice(11,-4) # el 11 es la posicion de la cadena donde queremos empezar sumando uno mas y el -4 es contando de izquierda hacia derecha hasta donde queremos terminar
sitio = website[slice] # forma 2

print(primer_nombre)
print(apellido)
print(nombre2)
print(nombre_invertido)
print(website[slice])
print(sitio)

