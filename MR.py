# Modulos Ramdom

import random

x = random.randint(1,6)
y = random.random()

mi_lista = ['Piedra', 'Papel', 'Tigera']
z = random.choice(mi_lista)


cartas = ['1','2','3','4','5','6','7','8','9','J','Q','K','A']

random.shuffle(cartas)

print(cartas) 