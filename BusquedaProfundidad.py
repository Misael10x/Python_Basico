import random
import time
import os

WIDTH, HEIGHT = 21, 21
maze = [['█'] * WIDTH for _ in range(HEIGHT)]

def carve(x, y):
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 < nx < WIDTH and 0 < ny < HEIGHT and maze[ny][nx] == '█':
            maze[y + dy // 2][x + dx // 2] = ' '
            maze[ny][nx] = ' '
            carve(nx, ny)
