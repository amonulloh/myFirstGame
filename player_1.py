#This Class for Player_1
import pygame
import window

x_a = window.Window.x_a
x_b = window.Window.x_b
y_a = window.Window.y_a
y_b = window.Window.y_b
radius = window.Window.radius
speed = window.Window.speed

from window import window

class Player_1():
    move_a = pygame.key.get_pressed()
    if move_a[pygame.K_LEFT] and x_a > 505 + radius:
        x_a -= speed
    if move_a[pygame.K_RIGHT] and x_a < 995 - radius:
        x_a += speed
    if move_a[pygame.K_UP] and y_a > radius:
        y_a -= speed
    if move_a[pygame.K_DOWN] and y_a < 495 - radius:
        y_a += speed

    pygame.draw.circle(window, (0, 0, 225), (x_a, y_a), 15)
    pass
class Player_2():
    move_b = pygame.key.get_pressed()
    if move_b[pygame.K_a] and x_b > radius:
        x_b -= speed

    if move_b[pygame.K_d] and x_b < 495 - radius:
        x_b += speed

    if move_b[pygame.K_w] and y_b > radius:
        y_b -= speed

    if move_b[pygame.K_s] and y_b < 495 - radius:
        y_b += speed

    pygame.draw.circle(window, (255, 0, 0), (x_b, y_b), 15)
    
    pass