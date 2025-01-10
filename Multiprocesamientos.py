from multiprocessing import Process, cpu_count
import time


def contador(num):
    cont = 0
    while cont < num:
        cont += 1

# cada maquina tiene un limite de nucleos si se pasa el limite deellos se hace mas lento
#ya que hasta que los nucleos se desacupen o se desacupen uno de ellos seguira el siguiente


def main():
    
    iniciar = time.perf_counter()
    a = Process(target=contador, args=(12500000,))
    b = Process(target=contador, args=(125000000,))
    c = Process(target=contador, args=(125000000,))
    d = Process(target=contador, args=(125000000,))
    e = Process(target=contador, args=(125000000,))
    f = Process(target=contador, args=(125000000,))
    g = Process(target=contador, args=(125000000,))
    h = Process(target=contador, args=(125000000,))
    
    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    
    
    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()
    
    fin = time.perf_counter()
    tiempo = fin - iniciar
    print("Finalizo", tiempo, "Segundos")
    
    print(cpu_count())



if __name__ == '__main__':
    main()
