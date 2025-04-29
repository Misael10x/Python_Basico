    opciones = ["Opción A", "Opción B", "Opción C"]
    votos = {opcion: 0 for opcion in opciones}
    cantidad = int(input("¿Cuántos votos quieres simular? "))
    for _ in range(cantidad):
        voto = choice(opciones)
        votos[voto] += 1
