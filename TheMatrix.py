import random
import time
import os

def matrix_effect(width=80, height=20, speed=0.05):
    chars = "01X#*@"
    columns = [0] * width
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        for i in range(height):
            line = "".join(random.choice(chars) if random.random() > 0.2 else " " for _ in range(width))
            print(line)
        time.sleep(speed)

matrix_effect()
