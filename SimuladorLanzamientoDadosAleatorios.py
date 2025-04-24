import random
import time

def lanzar_dados():
    print("Lanzando dados", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    total = dado1 + dado2
    print(f"\nDado 1: {dado1} | Dado 2: {dado2} -> Total: {total}")

def main():
    while True:
        lanzar_dados()
        otra = input("¿Lanzar otra vez? (s/n): ")
        if otra.lower() != 's':
            break

if __name__ == "__main__":
    main()
