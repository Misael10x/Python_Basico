import random
import os
import time

width = 40
height = 20
fire = [[0] * width for _ in range(height)]

def generate_fire():
    for i in range(width):
        fire[-1][i] = random.randint(0, 3)

def spread_fire():
    for y in range(height - 1, 0, -1):
        for x in range(1, width - 1):
            fire[y - 1][x] = (fire[y][x - 1] + fire[y][x] + fire[y][x + 1]) // 3

def render_fire():
    chars = " .:!*#%@"
    os.system("cls" if os.name == "nt" else "clear")
    for row in fire:
        print("".join(chars[min(int(c), len(chars) - 1)] for c in row))

while True:
    generate_fire()
    spread_fire()
    render_fire()
    time.sleep(0.1)
