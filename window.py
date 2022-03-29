#This Class for Window

import pygame

window = pygame.display.set_mode((1000, 500))

class Window():
    
    x_a = 940
    y_a = 440 
    width_a = 35
    height_a = 35

    speed = 5
    radius = 15

    x_b =60
    y_b = 60
    width_b = 35
    height_b = 35

    pass

class Play():
    window.fill((0, 0, 0))
    pygame.display.update()
    pass