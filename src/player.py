# This Class for Player and Bullets

import pygame
import os
from src.window import Window

pygame.init()

shoots = pygame.mixer.Sound(os.path.join("sounds/shoots.wav"))  # setting 1st player shoot sound
shoots2 = pygame.mixer.Sound(os.path.join("sounds/shoots2.wav"))  # setting 2nd player shoot sound
foot = pygame.mixer.Sound(os.path.join("sounds/footstep.mp3"))  # setting 1st player foot sound
foot2 = pygame.mixer.Sound(os.path.join("sounds/footstep2.mp3"))  # setting 2nd player foot sound
oh = pygame.mixer.Sound(os.path.join("sounds/oh_sound.mp3"))  # setting player voice during the impact of the bullet
foot.set_volume(1 / 3)  # setting foot sound volume
foot2.set_volume(1 / 3)

objects = []
bullets = []


class Players:
    """
    All the logic of the player is only in this class.
    It contains 9 functions, each function has its own
     action will be reported.
    It is automatically run when you run "main.py", it
     will be imported into "mygame.py"
    """

    def __init__(self, x, y, speed, keys, img, bspeed, bradius, bcolour, ph):

        self.x, self.y = x, y  # players coord (x, y)
        self.speed = speed  # players speed: 5
        self.position = 0  # players position: 0 - Right, 1 - Down, 2 - Left, 3 - Up
        self.keyUp = keys[0]  # key for moving up: W, Up
        self.keyDown = keys[1]  # key for moving down: S, Down
        self.keyRight = keys[3]  # key for moving right: D, Right
        self.keyLeft = keys[2]  # key for moving Left: L, Left
        self.keyShoot = keys[4]  # key for shooting: Space, Enter
        self.imgNum = 0  # for sprites walking
        self.img = img  # setting sprites (players image)
        self.image = pygame.transform.rotate(self.img[self.imgNum],
                                             -self.position * 90)  # transformation of sprites
        self.school = ph  # the name of group: FIVT, FUPM
        self.bspeed = bspeed  # bullets speed
        self.bradius = bradius  # bullets radius
        self.bcolour = bcolour  # bullets color
        self.timeLimit = 0  # time interval between shots
        self.timeNull = 0  # time interval for reloading bullets
        self.cartridges = 20  # number of bullets in a cartridge
        self.hp = 5  # heartpower
        self.rect = pygame.Rect(x, y, 48, 48)  # rectangle of sprites
        objects.append(self)  # add object to list objects

    def move(self):
        """
        This function responsible for moving of sprites.
        """
        self.image = pygame.transform.rotate(self.img[self.imgNum // 6],
                                             -self.position * 90)
        self.moveDown()
        self.moveUp()
        self.moveLeft()
        self.moveRight()
        self.Shoot()

    def moveDown(self):
        """
        This function responsible for moving Down.
        """
        key = pygame.key.get_pressed()
        if key[self.keyDown] and self.y < 682:
            self.rect.y += self.speed
            self.y += self.speed
            self.position = 1
            self.imgNum += 1
            for obj in objects:
                if obj != self and pygame.Rect.colliderect(self.rect, obj.rect):
                    self.rect.y -= self.speed
                    self.y -= self.speed
            # Walls:
            if 98 < self.x < 822 and (107 < self.y < 193 or
                                      507 < self.y < 590):
                self.y -= self.speed
                self.rect.y -= self.speed
            if (98 < self.x < 184 or 738 < self.x < 822) and \
                    (382 < self.y < 630):
                self.y -= self.speed
                self.rect.y -= self.speed
            if 258 < self.x < 666 and 265 < self.y < 430:
                self.y -= self.speed
                self.rect.y -= self.speed

    def moveUp(self):
        """
        This function responsible for moving Up.
        """
        key = pygame.key.get_pressed()
        if key[self.keyUp] and self.y > 30:
            self.rect.y -= self.speed
            self.y -= self.speed
            self.position = 3
            self.imgNum += 1
            for obj in objects:
                if obj != self and pygame.Rect.colliderect(self.rect, obj.rect):
                    self.rect.y += self.speed
                    self.y += self.speed
            # Walls
            if 98 < self.x < 822 and (105 < self.y < 193 or
                                      507 < self.y < 590):
                self.y += self.speed
                self.rect.y += self.speed
            if (98 < self.x < 184 or 738 < self.x < 822) and \
                    (107 < self.y < 310):
                self.y += self.speed
                self.rect.y += self.speed
            if 258 < self.x < 666 and 265 < self.y < 430:
                self.y += self.speed
                self.rect.y += self.speed

    def moveLeft(self):
        """
        This function responsible for moving Left.
        """
        key = pygame.key.get_pressed()
        if key[self.keyLeft] and self.x > 0:
            self.rect.x -= self.speed
            self.x -= self.speed
            self.position = 2
            self.imgNum += 1
            for obj in objects:
                if obj != self and pygame.Rect.colliderect(self.rect, obj.rect):
                    self.rect.x += self.speed
                    self.x += self.speed
            # Walls
            if (144 < self.x < 183 or 734 < self.x < 822) and \
                    (107 < self.y < 310 or 385 < self.y < 590):
                self.x += self.speed
                self.rect.x += self.speed
            if 304 < self.x < 666 and 265 < self.y < 430:
                self.x += self.speed
                self.rect.x += self.speed

    def moveRight(self):
        """
        This function responsible for moving Right.
        """
        key = pygame.key.get_pressed()
        if key[self.keyRight] and self.x < 952:
            self.rect.x += self.speed
            self.x += self.speed
            self.position = 0
            self.imgNum += 1
            for obj in objects:
                if obj != self and pygame.Rect.colliderect(self.rect, obj.rect):
                    self.rect.x -= self.speed
                    self.x -= self.speed
            # Walls
            if (98 < self.x < 183 or 734 < self.x < 822) and \
                    (107 < self.y < 310 or 385 < self.y < 590):
                self.x -= self.speed
                self.rect.x -= self.speed
            if 258 < self.x < 666 and 265 < self.y < 430:
                self.x -= self.speed
                self.rect.x -= self.speed

    def Shoot(self):
        """
        This function responsible for shooting of sprites.
        """
        key = pygame.key.get_pressed()
        if key[self.keyShoot] and self.timeNull == 0 and self.timeLimit == 0:
            Bullets(self, self.x, self.y, self.position, self.bradius,
                    self.bcolour, self.bspeed)

            if self == objects[0]:
                shoots.play()
            else:
                shoots2.play()
            self.timeLimit = 10
            self.cartridges -= 1
            if self.cartridges == 0:
                self.timeNull = 150
        if self.timeNull > 0:
            self.timeNull -= 1
            if self.timeNull == 0:
                self.cartridges = 20
        if self.timeLimit > 0:
            self.timeLimit -= 2
        if self.imgNum >= 12:
            if self == objects[0]:
                foot.play()
            else:
                foot2.play()
            self.imgNum = 0

    def damage(self, value):
        """
        This function responsible for heart power of sprites.
        """
        self.hp -= value
        oh.play()
        if self.hp <= 0:
            objects.remove(self)
            self.hp = 0

    def draw(self):
        """
        This function responsible for drawing of sprites and result.
        """
        Window.windows.blit(self.image, (self.x, self.y))
        if len(objects) < 2:  # after Game over drawing the result
            res_font = pygame.font.SysFont(None, 200)
            res = res_font.render(self.school + ' ' + 'WIN', True, 'aqua')
            res2 = res_font.render(self.school + ' ' + 'WIN', True, 'black')
            Window.windows.blit(res2, res2.get_rect(center=(Window.length /
                                                            2 + 3, Window.width / 2 + 3)))
            Window.windows.blit(res, res.get_rect(center=(Window.length /
                                                          2, Window.width / 2)))
        self.results()

    @staticmethod
    def results():
        """
        This function responsible for result of the game.
        """
        j = 0
        result_font = pygame.font.SysFont(None, 35)
        for obj in objects:
            result = result_font.render(obj.school + ': ' + str(obj.hp) +
                                        '   ' + str(obj.cartridges), True, obj.bcolour)
            Window.windows.blit(result, (50 + j * 50, 3))
            j += 16


class Bullets:
    """
    All the logic of the bullets in this class.
    It contains 2 functions, each function has its own
     action will be reported.
    It is automatically run when you run "main.py", it
     will be called in the class "Players".
    """

    def __init__(self, parent, x, y, position, radius, colour, speed):
        bullets.append(self)

        self.x, self.y = x + 24, y + 24  # bullets coord (x, y)
        self.position = position  # bullets position: 0 - Right, 1 - Down, 2 - Left, 3 - Up
        self.radius = radius  # bullets radius: 4
        self.colour = colour  # bullets color: white, aqua
        self.speed = speed  # bullets speed: 20
        self.parent = parent  # bullets parent: FIVT or FUPM
        self.damage = 1  # number of shots

    def moveSh(self):
        """
        This function responsible for moving of bullets.
        """
        if self.position == 0:  # moving Right
            self.x += self.speed
        if self.position == 1:  # moving Down
            self.y += self.speed
        if self.position == 2:  # moving Left
            self.x -= self.speed
        if self.position == 3:  # moving Up
            self.y -= self.speed
        # Walls
        if 306 <= self.x <= 664 and 313 <= self.y <= 431:
            bullets.remove(self)
        if 184 <= self.x <= 782 and (153 <= self.y <= 192 or 554 <= self.y <= 590):
            bullets.remove(self)
        if (144 <= self.x <= 184 or 782 <= self.x <= 822) and \
                (153 <= self.y <= 314 or 433 <= self.y <= 592):
            bullets.remove(self)
        if self.x <= 0 or self.x > Window.length or self.y <= 30 or self.y > Window.width:
            bullets.remove(self)
        # Damaging to another player
        else:
            for obj in objects:
                if obj != self.parent and obj.rect.collidepoint(self.x, self.y):
                    obj.damage(self.damage)
                    bullets.remove(self)
                    break

    def drawSh(self):
        """
        This function responsible for drawing of bullets.
        """
        pygame.draw.circle(Window.windows, self.colour, (self.x, self.y), self.radius)
