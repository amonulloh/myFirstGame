# dCS_2D

import pygame
import os

import src.player as player
from src.window import Window as window
from src.player import Players
from src.player import Base

pygame.init()

clock = pygame.time.Clock()
fps = 60  # frames per second

# setting caption of screen
pygame.display.set_caption("PhS_2D")
icon = pygame.image.load(os.path.join('images', 'icon.png'))
pygame.display.set_icon(icon)
# uploading images from folder images
menu_img = pygame.image.load(os.path.join('images', 'cs_menu.png'))
play_img = pygame.image.load(os.path.join('images', 'play.jpg'))
ph_img = pygame.image.load(os.path.join('images', 'phystech.png'))
restart_img = pygame.image.load(os.path.join('images', 'restart.jpg'))
exit_img = pygame.image.load(os.path.join('images', 'exit.jpg'))
pause_img = pygame.image.load(os.path.join('images', 'pause2.jpg'))
sound_on = pygame.image.load(os.path.join('images', 'sound_on.jpg'))
sound_off = pygame.image.load(os.path.join('images', 'sound_off.jpg'))
field = pygame.image.load(os.path.join('images', 'map_cs.png'))
# scaling the uploaded images in their size
menu_img = pygame.transform.scale(menu_img, (1000, 730))
play_img = pygame.transform.scale(play_img, (200, 45))
ph_img = pygame.transform.scale(ph_img, (70, 70))
restart_img = pygame.transform.scale(restart_img, (200, 45))
exit_img = pygame.transform.scale(exit_img, (200, 45))
pause_img = pygame.transform.scale(pause_img, (30, 30))
sound_on = pygame.transform.scale(sound_on, (50, 50))
sound_off = pygame.transform.scale(sound_off, (50, 50))
# font and size of output texts
header_font = pygame.font.SysFont('myanmartext', 60)
restart_font = pygame.font.SysFont('georgia', 40)
d2_font = pygame.font.SysFont('inkfree', 50)
# setting of main menu texts. name_tex_2 for shadow
header_text = header_font.render('PHYSTECH STRIKE', True, 'white')
header_text_2 = header_font.render('PHYSTECH STRIKE', True, 'black')
restart_text = restart_font.render('RESTART', True, 'black')
restart_text_2 = restart_font.render('RESTART', True, 'white')
d2_text = d2_font.render('2D', True, 'red')
d2_text_2 = d2_font.render('2D', True, 'black')
# uploading sprites and objects image
image1 = [pygame.image.load(os.path.join('images', 'soldier11.png')),
          pygame.image.load(os.path.join('images', 'soldier12.png'))]
image2 = [pygame.image.load(os.path.join('images', 'soldier21.png')),
          pygame.image.load(os.path.join('images', 'soldier22.png'))]
image3 = pygame.image.load(os.path.join('images', 'fupm.png'))
image3 = pygame.transform.scale(image3, (68, 68))
image4 = pygame.image.load(os.path.join('images', 'fivt.jpg'))
image4 = pygame.transform.scale(image4, (68, 68))
# add music to main menu and soldier voice
pygame.mixer.music.load(os.path.join('sounds', 'cs_theme.mp3'))
go_sound = pygame.mixer.Sound(os.path.join("sounds/go_sound.mp3"))


# object's (player) characters
def sprites():
    """
    This function responsible for sprites and
     objects characters
    """
    Players(50, 100, 5, (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d,
                         pygame.K_SPACE), image1, 20, 4, 'grey', 'FUPM')
    Players(940, 440, 5, (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT,
                          pygame.K_RIGHT, pygame.K_RETURN), image2, 20, 4, 'yellow', 'FIVT')
    Base(68, 220, image3, 'grey', 'FUPM')
    Base(824, 450, image4, 'yellow', 'FIVT')


class Game:
    """
    Part the logic of the game in this class.
    It contains 3 functions, each function has its own
     action will be reported.
    It is automatically run when you run "main.py".
    To work with it, you need to generate an example
     of it.
    """

    def __init__(self):
        self.active = False
        self.result = False
        self.music = True
        self.sound = True
        self.fivt = 0
        self.fupm = 0
        self.on = 1  # for on/off sounds

    def start(self):
        """
        This function is the main one (run the code).
        Responsible for running, the "play", "restart",
         "exit" and "sound" buttons.
        """
        if self.music:
            pygame.mixer.music.play(-1)
        play = True
        while play:
            if not self.music:
                pygame.mixer.music.play(-1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                if event.type == pygame.KEYDOWN:
                    # esc responsible for pause the game
                    if event.key == pygame.K_ESCAPE:
                        if self.on == 1:
                            self.music = True
                        else:
                            self.music = False
                        self.active = False
                    if event.key == pygame.K_TAB:
                        self.result = True
                    else:
                        self.result = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    # this condition responsible for play button
                    if 50 <= x <= 250 and 330 <= y <= 375:
                        self.active = True
                        self.music = False
                        go_sound.play()
                    # this condition responsible for restart button
                    if (50 < x <= 250 and 400 <= y <= 445 and not self.active) or \
                            (len(player.objects) == 3 and 400 <= x <= 600 and
                             470 <= y <= 515):
                        if len(player.objects) < 4:
                            if player.objects[0].school == 'FUPM' and \
                                    player.objects[1].school == 'FIVT':
                                if player.objects[2].school == 'FUPM':
                                    self.fupm += 1
                                else:
                                    self.fivt += 1
                            else:
                                if player.objects[0].school == 'FUPM':
                                    self.fupm += 1
                                else:
                                    self.fivt += 1
                        self.active = True
                        self.music = False
                        player.objects = []
                        player.bullets = []
                        sprites()
                        go_sound.play()
                    # this condition responsible for exit button
                    if 50 <= x <= 250 and 470 <= y <= 515 and not self.active:
                        play = False
                    # this condition responsible for pause button
                    if 485 <= x <= 515 and 0 <= y <= 30 and self.active:
                        if self.on == 0:
                            self.music = True
                        else:
                            self.music = False
                        self.active = False
                    # this condition responsible for sound button
                    if 50 <= x <= 100 and 600 <= y <= 650 and not self.active:
                        if self.on % 2 == 0:
                            self.musics()
                            self.music = False
                            self.sound = False
                        else:
                            self.musics()
                            self.music = True
                            self.sound = True
                        self.on += 1
                        if self.on == 2:
                            self.on = 0
            self.display()

    def display(self):
        """
        This function displays widgets in a screen.
        """
        if not self.active:  # main menu
            window.windows.blit(menu_img, (0, 0))
            window.windows.blit(header_text_2, (53, 88))
            window.windows.blit(header_text, (50, 85))
            window.windows.blit(d2_text_2, (514, 122))
            window.windows.blit(d2_text, (512, 120))
            window.windows.blit(play_img, (50, 330))
            window.windows.blit(restart_img, (50, 400))
            window.windows.blit(exit_img, (50, 470))
            window.windows.blit(ph_img, (930, 660))
            if self.sound:
                window.windows.blit(sound_on, (50, 600))
            if not self.sound:
                window.windows.blit(sound_off, (50, 600))
        elif self.active:  # running game
            window.windows.fill((0, 0, 0))
            window.windows.blit(field, (0, 30))
            if len(player.objects) > 3:  # before game over
                for obj in player.objects:
                    obj.move()
                for bul in player.bullets:
                    bul.move_bullets()
                for obj in player.objects:
                    obj.draw()
                for bul in player.bullets:
                    bul.draw_bullets()
                window.windows.blit(pause_img, (485, 0))
            else:  # after game over
                for obj in player.objects:
                    obj.draw()
                window.windows.blit(restart_text, (400, 450))
                window.windows.blit(restart_text_2, (401, 451))
                go_sound.stop()
                window.windows.blit(pause_img, (450, -1))
        if self.result:
            pygame.draw.rect(window.windows, 'grey', (305, 313, 357, 118))
            result_text = header_font.render('FUPM:  ' + str(self.fupm),
                                             True, 'black')
            result_text2 = header_font.render('FIVT:  ' + str(self.fivt),
                                              True, 'black')
            window.windows.blit(result_text, (340, 310))
            window.windows.blit(result_text2, (340, 360))

        pygame.display.update()
        clock.tick(fps)

    def musics(self):
        """
        This function responsible for on/off of sounds game.
        """
        player.shoots.set_volume(self.on)
        player.shoots2.set_volume(self.on)
        player.foot.set_volume(self.on / 3)
        player.foot2.set_volume(self.on / 3)
        player.oh.set_volume(self.on)
        go_sound.set_volume(self.on)


sprites()

"""
__init__(self, parent, x, y, position,
              radius, colour, speed)
-moveSh(self): list
-drawSh(self): list

"""
