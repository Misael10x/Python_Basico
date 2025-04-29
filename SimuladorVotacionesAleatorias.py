def simulador_votacion():
    opciones = ["Opción A", "Opción B", "Opción C"]
    votos = {opcion: 0 for opcion in opciones}
    
    cantidad = int(input("¿Cuántos votos quieres simular? "))
    from random import choice
    for _ in range(cantidad):
        voto = choice(opciones)
        votos[voto] += 1

    print("\nResultados:")
    for opcion, cantidad in votos.items():
        print(f"{opcion}: {cantidad} votos")

def main():
    simulador_votacion()

if __name__ == "__main__":
    main()
