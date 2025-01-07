import threading
import time

def tiempo():
    print()
    print()
    contador = 0
    while True:
        time.sleep(1)
        contador += 1
        print(contador, "Segundos")
