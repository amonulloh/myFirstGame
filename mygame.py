# dCS_2D

import pygame

import player
import window
# import bullet
from player import Players

pygame.init()

clock = pygame.time.Clock()
fps = 30

pygame.display.set_caption("CS_2D")
menu_img = pygame.image.load('cs_menu.png')
menu_img = pygame.transform.scale(menu_img, (1000, 730))
play_img = pygame.image.load('play.jpg')
play_img = pygame.transform.scale(play_img, (200, 45))
restart_img = pygame.image.load('restart.jpg')
restart_img = pygame.transform.scale(restart_img, (200, 45))
options_img = pygame.image.load('options.jpg')
options_img = pygame.transform.scale(options_img, (200, 45))
exit_img = pygame.image.load('exit.jpg')
exit_img = pygame.transform.scale(exit_img, (200, 45))
header_font = pygame.font.SysFont('myanmartext', 60)
header_text = header_font.render('PHYSTECH STRIKE', True, 'white')
header_text_2 = header_font.render('PHYSTECH STRIKE', True, 'black')
d2_font = pygame.font.SysFont('inkfree', 50)
d2_text = d2_font.render('2D', True, 'red')
d2_text_2 = d2_font.render('2D', True, 'black')

pygame.mixer.music.load('cs_theme.mp3')

image1 = [pygame.image.load('soldier11.png'), pygame.image.load('soldier12.png')]
image2 = [pygame.image.load('soldier21.png'), pygame.image.load('soldier22.png')]
map = pygame.image.load('map_cs.png')

Players(60, 60, 8, (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE), image2, 20, 4, 'white', 'FUPM')
Players(940, 440, 8, (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RETURN), image1, 20,
        4, 'blue', 'FIVT')
# player1 = Players(x, y, speed, (keys), image, bulspeed, bulradius, bulcolour)

play = True
active = False
game_over = False
music = True
if music:
    pygame.mixer.music.play(-1)
while play:
    if not music:
        pygame.mixer.music.play(-1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
            if 50 <= x <= 250 and 330 <= y <= 375:
                active = True
                music = False
            if 50 <= x <= 250 and 400 <= y <= 445 and not active:
                active = True
                music = False
                player.objects = []
                player.bullets = []
                Players(60, 60, 8, (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE), image2, 50, 4,
                        'white', 'FUPM')
                Players(940, 440, 8, (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RETURN),
                        image1, 50,
                        4, 'blue', 'FIVT')
            if 50 <= x <= 250 and 540 <= y <= 590 and not active:
                play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                music = True
                active = False
    if not active:
        window.windows.blit(menu_img, (0, 0))
        window.windows.blit(header_text_2, (53, 88))
        window.windows.blit(header_text, (50, 85))
        window.windows.blit(d2_text_2, (514, 122))
        window.windows.blit(d2_text, (512, 120))
        window.windows.blit(play_img, (50, 330))
        window.windows.blit(restart_img, (50, 400))
        window.windows.blit(options_img, (50, 470))
        window.windows.blit(exit_img, (50, 540))
    elif active:
        window.windows.fill((0, 0, 0))
        window.windows.blit(map, (0, 30))
        if len(player.objects) > 1:
            for obj in player.objects: obj.move()
            for bul in player.bullets: bul.moveSh()
            for obj in player.objects: obj.draw()
            for bul in player.bullets: bul.drawSh()
        else:
            for obj in player.objects: obj.draw()






    pygame.display.update()
    clock.tick(fps)
