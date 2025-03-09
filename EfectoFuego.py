import random
import os
import time

width = 40
height = 20
fire = [[0] * width for _ in range(height)]

def generate_fire():
    for i in range(width):
        fire[-1][i] = random.randint(0, 3)
