import time

def cronometro():
    input("Presiona ENTER para iniciar el cronómetro...")
    inicio = time.time()
    input("Presiona ENTER para detener el cronómetro.")
    fin = time.time()
    transcurrido = fin - inicio
    print(f"Tiempo transcurrido: {round(transcurrido, 2)} segundos.")

cronometro()
