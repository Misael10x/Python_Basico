# Metodo Format

#str.format() =

str_1 = 'leche'
str_2 = 'casar'

#print('Arroz con leche me quiero casar')
#print('Arroz con '+ str_1 + ' me quiero ' + str_2)
#print('Arroz con {0}  me quiero {1}'.format(str_1, str_2))
#print('Arroz con {str_2}  me quiero {str_1}'.format(str_1 = str_1 , str_2 = str_2))

texto = 'Arroz con {} me quiero {}'
#print(texto.format(str_1, str_2))
nombre = 'Misael'

#print('Hola, mi nombre es {}'.format(nombre))

#print('Hola, mi nombre es {:10}. mucho gusto :)'.format(nombre))

#print('Hola, mi nombre es {:<10}. mucho gusto :)'.format(nombre)) alinear a la izquierda 

#print('Hola, mi nombre es {:>10}. mucho gusto :)'.format(nombre))  alinear a la derecha

#print('Hola, mi nombre es {:^10}. mucho gusto :)'.format(nombre)) # centrar




numero = 1000
#print('El numero PI es: {:.2f}'.format(numero))   numero en decimal

#print('El numero PI es: {:b}'.format(numero))    numero binario

#print('El numero PI es: {:o}'.format(numero))  numero octal

#print('El numero PI es: {:x}'.format(numero))  numero en hexadecima
 
#print('El numero PI es: {:e}'.format(numero)) numero en notacion cientifica