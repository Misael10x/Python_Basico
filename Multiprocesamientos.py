from multiprocessing import Process, cpu_count
import time


def contador(num):
    cont = 0
    while cont < num:
        cont += 1

# cada maquina tiene un limite de nucleos si se pasa el limite deellos se hace mas lento
#ya que hasta que los nucleos se desacupen o se desacupen uno de ellos seguira el siguiente

