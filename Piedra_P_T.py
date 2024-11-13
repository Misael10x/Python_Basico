import random

lista = ['piedra', 'papel', 'tigera']

while True:
    computadora = random.choice(lista)
    jugador = None

    while jugador not in lista:
        jugador = input('piedra, papel o tigera: ').lower()

    if jugador == computadora:
        print('computadora', computadora)
        print('jugador', jugador)
        print('empate')
    elif jugador == 'piedra':
        if computadora == 'papel':
           print('computadora ', computadora)
           print('jugador', jugador)
           print('pedistes')
    if computadora == 'tigera':
        print('computadora ', computadora)
        print('jugador', jugador)
        print('ganamos')
    elif jugador == 'papel':
     if computadora == 'tigera':
        print('computadora ', computadora)
        print('jugador', jugador)
        print('pedistes')
     if computadora == 'roca':
        print('computadora ', computadora)
        print('jugador', jugador)
        print('ganamos')
    elif jugador == 'tigera':
        if computadora == 'piedra':
          print('computadora ', computadora)
          print('jugador', jugador)
          print('pedistes')
    if computadora == 'papel':
        print('computadora ', computadora)
        print('jugador', jugador)
        print('ganamos')


        
    jugar_de_nuevo = input('quieres jugar de nuevo? (si/no) ').lower()
    if jugar_de_nuevo != 'si':
        break