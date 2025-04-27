import time

def cronometro(segundos):
    for i in range(segundos, 0, -1):
        print(f"Tiempo restante: {i} segundos", end="\r", flush=True)
        time.sleep(1)
    print("\n¡Tiempo terminado!")

def main():
    tiempo = int(input("Ingresa el tiempo en segundos: "))
    cronometro(tiempo)

if __name__ == "__main__":
    main()
