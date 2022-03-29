#This Class for Bullets

#dCS_2D

import pygame
pygame.init()

window = pygame.display.set_mode((1000, 500))

pygame.display.set_caption("CS_2D")



x_a = 940
y_a = 440 
width_a = 35
height_a = 35
speed_a = 5
radius = 15

x_b =60
y_b = 60
width_b = 35
height_b = 35 
speed_b = 5

play = True

while play:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

       
    move_a = pygame.key.get_pressed()
    if move_a[pygame.K_LEFT] and x_a > 505 + radius:
        x_a -= speed_a
    if move_a[pygame.K_RIGHT] and x_a < 995 - radius:
        x_a += speed_a
    if move_a[pygame.K_UP] and y_a > radius:
        y_a -= speed_a
    if move_a[pygame.K_DOWN] and y_a < 495 - radius:
        y_a += speed_a

    
    window.fill((0, 0, 0))
    pygame.draw.circle(window, (0, 0, 225), (x_a, y_a), 15)

    move_b = pygame.key.get_pressed()
    if move_b[pygame.K_a] and x_b > radius:
        x_b -= speed_b

    if move_b[pygame.K_d] and x_b < 495 - radius:
        x_b += speed_b

    if move_b[pygame.K_w] and y_b > radius:
        y_b -= speed_b

    if move_b[pygame.K_s] and y_b < 495 - radius:
        y_b += speed_b
    

    pygame.draw.circle(window, (255, 0, 0), (x_b, y_b), 15)
    pygame.display.update()


