import threading
import time


def desayunar():
    print('Iniciando...desayuno')
    time.sleep(3)
    print('Finalizando...')

def tomar_cafe():
    print('Iniciando...tomar cafe')
    time.sleep(4)
    print('Finalizando...')
    
def estudiar():  
    print('Iniciando...estuduar')
    time.sleep(5)
    print('Finalizando...')

inicio = time.perf_counter()

x = threading.Thread(target=desayunar, args=())
x.start()

y = threading.Thread(target=tomar_cafe, args=())
y.start()


z = threading.Thread(target=estudiar, args=())
z.start()

x.join() # sincronizacion de hilos
y.join()
z.join()

#desayunar()
#tomar_cafe()
#estudiar()

print(threading.active_count())
print(threading.enumerate())

fin = time.perf_counter()
tiempo = fin - inicio
print(tiempo)
