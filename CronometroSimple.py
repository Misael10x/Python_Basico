import time

def cronometro(segundos):
    for i in range(segundos, 0, -1):
        print(f"Tiempo restante: {i} segundos", end="\r", flush=True)
