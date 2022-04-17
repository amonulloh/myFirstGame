#This Class for Player_1

import pygame
import window
from bullet import Bullets

class Players():
    def __init__(self, x, y, speed, keys, img, bulspeed, bulradius, bulcolour):

        self.x, self.y = x, y
        self.speed = speed
        self.position = 0
        self.keyUp = keys[0]
        self.keyDown = keys[1]
        self.keyRight = keys[3]
        self.keyLeft = keys[2]
        self.keyShoot = keys[4]
        self.imgNum = 0
        self.img = img
        self.image = pygame.transform.rotate(self.img[self.imgNum], -self.position * 90)

        self.bulspeed = bulspeed
        self.bulradius = bulradius
        self.bulcolour = bulcolour

    def move(self):
        self.image = pygame.transform.rotate(self.img[self.imgNum], -self.position * 90)
        key = pygame.key.get_pressed()
        if key[self.keyDown] and self.y < 652:
            self.y += self.speed
            self.position = 1
            self.imgNum += 1
        if key[self.keyUp] and self.y > 0:     
            self.y -= self.speed
            self.position = 3
            self.imgNum += 1
        if key[self.keyLeft] and self.x > 0:
            self.x -= self.speed
            self.position = 2
            self.imgNum += 1
        if key[self.keyRight] and self.x < 952:
            self.x += self.speed
            self.position = 0
            self.imgNum += 1

        if key[self.keyShoot]:
            Bullets(self.x + 24, self.y + 24, self.position, self.bulradius, self.bulcolour, self.bulspeed)

        if self.imgNum >= 6:
            self.imgNum = 0
        
        

    def draw(self):
        window.windows.blit(self.image, (self.x, self.y))
        

