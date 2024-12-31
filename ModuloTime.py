import time


#print(time.ctime(0))

#print(time.time())

#print(time.ctime(time.time()))

#tiempo_actual = time.localtime()
#print(tiempo_actual)

#tiempo_actual = time.localtime()

#tiempo_actual = time.gmtime()
#tiempo = time.strftime("%B %d %y %H:%M:%S", tiempo_actual)
#print(tiempo)

#cadena_tiempo = '18 November, 2024'
#tiempo = time.strptime(cadena_tiempo, '%d %B, %Y')
#print(tiempo)

tiempo_tupla = (2024, 11, 18, 18, 58, 0, 0, 0, 0)
cadena_tiempo = time.asctime(tiempo_tupla)
print(cadena_tiempo)
