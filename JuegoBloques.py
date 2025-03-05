import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Bloques")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 100
player_speed = 5

block_size = 50
blocks = []
for i in range(5):
    x = random.randint(0, WIDTH - block_size)
    y = random.randint(0, HEIGHT // 2)
    blocks.append(pygame.Rect(x, y, block_size, block_size))

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    
    player = pygame.Rect(player_x, player_y, player_size, player_size)
    pygame.draw.rect(screen, RED, player)
    
    for block in blocks:
        pygame.draw.rect(screen, RED, block)
    
    pygame.display.update()
    
pygame.quit()
