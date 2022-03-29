#dCS_2D

import pygame
import window

from player_1 import Player

pygame.init()

pygame.display.set_caption("CS_2D")

player1 = Player(940, 440, 15, (0, 0, 255), 5)
player2 = Player(60, 60, 15, (255, 0 ,0), 5)


play = True

while play:
    pygame.time.delay(10)
    window.windows.fill((0, 0, 0))
    player1.move(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    player1.draw()
    player2.move(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    player2.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    pygame.display.update()
