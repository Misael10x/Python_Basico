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

def solve(x, y, path=[]):
    if (x, y) == (WIDTH - 2, HEIGHT - 2):
        for px, py in path:
            maze[py][px] = '.'
        return True
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if maze[ny][nx] == ' ':
            maze[ny][nx] = '.'
            if solve(nx, ny, path + [(nx, ny)]):
                return True
            maze[ny][nx] = ' '
    return False

maze[1][1] = ' '
carve(1, 1)
solve(1, 1)

def display():
    os.system("cls" if os.name == "nt" else "clear")
    for row in maze:
        print("".join(row))
    time.sleep(0.05)

display()
