# dCS_2D

import pygame
import os

import src.player as player
from src.window import Window as window
from src.player import Players

pygame.init()

clock = pygame.time.Clock()
fps = 60  # frames per second

pygame.display.set_caption("PhS_2D")  # setting caption of screen
icon = pygame.image.load(os.path.join('images', 'icon.png'))
pygame.display.set_icon(icon)  # setting icon of screen
menu_img = pygame.image.load(os.path.join('images', 'cs_menu.png'))  # setting menu image
menu_img = pygame.transform.scale(menu_img, (1000, 730))  # scale the menu image in size 1000x700
play_img = pygame.image.load(os.path.join('images', 'play.jpg'))  # play button image
play_img = pygame.transform.scale(play_img, (200, 45))  # scale in size 200x45
ph_img = pygame.image.load(os.path.join('images', 'phystech.png'))  # phystech icon image
ph_img = pygame.transform.scale(ph_img, (70, 70))  # scale in size 70x07
restart_img = pygame.image.load(os.path.join('images', 'restart.jpg'))  # restart button image
restart_img = pygame.transform.scale(restart_img, (200, 45))  # scale in size 200x45
exit_img = pygame.image.load(os.path.join('images', 'exit.jpg'))  # exit button image
exit_img = pygame.transform.scale(exit_img, (200, 45))  # scale in size 200x45
pause_img = pygame.image.load(os.path.join('images', 'Screenshot_1.png'))  # pause button image
pause_img = pygame.transform.scale(pause_img, (100, 31))  # scale in size 100x31
sound_on = pygame.image.load(os.path.join('images', 'sound_on.jpg'))  # sound on button image
sound_on = pygame.transform.scale(sound_on, (50, 50))  # scale in size 50x50
sound_off = pygame.image.load(os.path.join('images', 'sound_off.jpg'))  # sound off button image
sound_off = pygame.transform.scale(sound_off, (50, 50))  # scale in size 50x50
header_font = pygame.font.SysFont('myanmartext', 60)  # the font of header text
header_text = header_font.render('PHYSTECH STRIKE', True, 'white')  # game name in the main menu
header_text_2 = header_font.render('PHYSTECH STRIKE', True, 'black')  # game name shadow
restart_font = pygame.font.SysFont('georgia', 40)  # restart text font
restart_text = restart_font.render('RESTART', True, 'black')  # restart text after game over
restart_text_2 = restart_font.render('RESTART', True, 'white')  # restart text shadow
d2_font = pygame.font.SysFont('inkfree', 50)  # "2D" font
d2_text = d2_font.render('2D', True, 'red')  # text "2D"
d2_text_2 = d2_font.render('2D', True, 'black')  # text "2D" shadow

image1 = [pygame.image.load(os.path.join('images', 'soldier11.png')),  # add the 1st sprite of the 1st player
          pygame.image.load(os.path.join('images', 'soldier12.png'))]  # add the 2nd sprite of the 1st player
image2 = [pygame.image.load(os.path.join('images', 'soldier21.png')),  # add the 1st sprite of the 2nd player
          pygame.image.load(os.path.join('images', 'soldier22.png'))]  # add the 2st sprite of the 2nd player
map = pygame.image.load(os.path.join('images', 'map_cs.png'))  # add map of the game

Players(60, 60, 5, (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d,
                    pygame.K_SPACE), image2, 20, 4, 'white', 'FUPM')  # 1st object's (player) characters
Players(940, 440, 5, (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT,
                      pygame.K_RIGHT, pygame.K_RETURN), image1, 20,
        4, 'aqua', 'FIVT')  # 2nd object's (player) characters
# Players(x, y, speed, (keys), image, bspeed, bradius, bcolour, ph)

pygame.mixer.music.load(os.path.join('sounds', 'cs_theme.mp3'))  # add theme music to main menu
go_sound = pygame.mixer.Sound(os.path.join("sounds/go_sound.mp3"))  # add player voice sound


class Game:
    @staticmethod
    def start():
        """
        This function is the main one (run the code).
        Responsible for running, the "play", "restart",
         "exit" and "sound" buttons.
        """
        active = False
        music = True
        sound = True
        i = 0  # for on/off sounds
        if music:
            pygame.mixer.music.play(-1)
        play = True
        while play:
            if not music:
                pygame.mixer.music.play(-1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # esc responsible for pause the game
                        if i == 0:
                            music = True
                        else:
                            music = False
                        active = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 50 <= x <= 250 and 330 <= y <= 375:  # responsible for play button
                        active = True
                        music = False
                        go_sound.play()
                    if (50 <= x <= 250 and 400 <= y <= 445 and not active) or \
                            (len(player.objects) == 1 and 400 <= x <= 600 and
                             470 <= y <= 515):  # responsible for restart button
                        active = True
                        music = False
                        player.objects = []
                        player.bullets = []
                        Players(60, 60, 5, (pygame.K_w, pygame.K_s,
                                pygame.K_a, pygame.K_d, pygame.K_SPACE),
                                image2, 20, 4, 'white', 'FUPM')
                        Players(940, 440, 5, (pygame.K_UP, pygame.K_DOWN,
                                pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RETURN),
                                image1, 20, 4, 'aqua', 'FIVT')
                        go_sound.play()
                    if 50 <= x <= 250 and 470 <= y <= 515 and not active:  # responsible for exit button
                        play = False
                    if 450 <= x <= 550 and 0 <= y <= 30 and active:  # responsible for pause button
                        if i == 0:
                            music = True
                        else:
                            music = False
                        active = False
                    if 50 <= x <= 100 and 600 <= y <= 650 and not active:  # responsible for sound button
                        if i % 2 == 0:
                            Game.musics(i)
                            music = False
                            sound = False
                        else:
                            Game.musics(i)
                            music = True
                            sound = True
                        i += 1
                        if i == 2:
                            i = 0
            if active == False:  # main menu
                window.windows.blit(menu_img, (0, 0))
                window.windows.blit(header_text_2, (53, 88))
                window.windows.blit(header_text, (50, 85))
                window.windows.blit(d2_text_2, (514, 122))
                window.windows.blit(d2_text, (512, 120))
                window.windows.blit(play_img, (50, 330))
                window.windows.blit(restart_img, (50, 400))
                window.windows.blit(exit_img, (50, 470))
                window.windows.blit(ph_img, (930, 660))
                if sound:
                    window.windows.blit(sound_on, (50, 600))
                if not sound:
                    window.windows.blit(sound_off, (50, 600))
            elif active:  # running game
                window.windows.fill((0, 0, 0))
                window.windows.blit(map, (0, 30))
                if len(player.objects) > 1:  # before game over
                    for obj in player.objects: obj.move()
                    for bul in player.bullets: bul.moveSh()
                    for obj in player.objects: obj.draw()
                    for bul in player.bullets: bul.drawSh()
                    window.windows.blit(pause_img, (450, -1))
                else:  # after game over
                    for obj in player.objects: obj.draw()
                    window.windows.blit(restart_text, (400, 450))
                    window.windows.blit(restart_text_2, (401, 451))
                    go_sound.stop()
                    window.windows.blit(pause_img, (450, -1))
            pygame.display.update()
            clock.tick(fps)

    @staticmethod
    def musics(i):
        """
        This function responsible for on/off of sounds game.
        """
        player.shoots.set_volume(i)
        player.shoots2.set_volume(i)
        player.foot.set_volume(i / 3)
        player.foot2.set_volume(i / 3)
        player.oh.set_volume(i)
        go_sound.set_volume(i)
