#dCS_2D

import pygame
import window

import bullet
from player import Players

pygame.init()
clock = pygame.time.Clock()
fps = 20

pygame.display.set_caption("CS_2D")
image1 = [pygame.image.load('soldier11.png'), pygame.image.load('soldier11.png'), pygame.image.load('soldier11.png'), 
        pygame.image.load('soldier12.png'), pygame.image.load('soldier12.png'), pygame.image.load('soldier12.png')]
image2 = [pygame.image.load('soldier21.png'), pygame.image.load('soldier21.png'), pygame.image.load('soldier21.png'), 
        pygame.image.load('soldier22.png'), pygame.image.load('soldier22.png'), pygame.image.load('soldier22.png')]

player1 = Players(940, 440, 10, (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RETURN), image1, 50, 3, 'black')
player2 = Players(60, 60, 10, (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE), image2, 50, 3, 'white')

#player1 = Players(x, y, speed, (keys), image, bulspeed, bulradius, bulcolour)

map = pygame.image.load('map_cs.png')

play = True

while play:
    window.windows.blit(map, (0, 0))
    for bul in bullet.bullets: bul.drawSh()
    player1.move()
    player1.draw()
    player2.move()
    player2.draw()
    for bul in bullet.bullets: bul.moveSh()
    for bul in bullet.bullets: bul.drawSh()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    pygame.display.update()
    clock.tick(fps)
