import time
import random

player1 = "🧑"
player2 = "🤺"
p1_health = 10
p2_health = 10

def display(p1, p2, h1, h2):
    print(f"\n{player1} {'❤️' * h1}   VS   {'❤️' * h2} {player2}")
    print(" " * random.randint(5, 15) + "⚔️")
