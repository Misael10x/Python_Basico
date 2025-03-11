import time
import random

player1 = "🧑"
player2 = "🤺"
p1_health = 10
p2_health = 10

def display(p1, p2, h1, h2):
    print(f"\n{player1} {'❤️' * h1}   VS   {'❤️' * h2} {player2}")
    print(" " * random.randint(5, 15) + "⚔️")

while p1_health > 0 and p2_health > 0:
    display(player1, player2, p1_health, p2_health)
    time.sleep(1)
    
    if random.choice([True, False]):
        p2_health -= 1
        print(f"{player1} ataca a {player2} ⚔️🔥")
    else:
        p1_health -= 1
        print(f"{player2} ataca a {player1} ⚔️🔥")
    
    time.sleep(1)

winner = player1 if p1_health > 0 else player2
print(f"\n🏆 {winner} GANA LA BATALLA ⚔️🎉")
