# This Class for Player_1

import pygame
import window

pygame.init()

objects = []
bullets = []

class Players:
    def __init__(self, x, y, speed, keys, img, bulspeed, bulradius, bulcolour, ph):
        self.type = 'player'

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
        self.school = ph

        self.bulspeed = bulspeed
        self.bulradius = bulradius
        self.bulcolour = bulcolour
        self.timeLimit = 0
        self.timeNull = 0
        self.i = 0
        self.hp = 5
        self.buldam = 1
        self.rect = pygame.Rect(x, y, 48, 48)
        objects.append(self)

    def move(self):
        self.image = pygame.transform.rotate(self.img[self.imgNum // 3], -self.position * 90)
        key = pygame.key.get_pressed()

        if key[self.keyDown] and self.y < 682:
            self.rect.y += self.speed
            self.y += self.speed
            self.position = 1
            self.imgNum += 1
            if 98 < self.x < 822 and (107 < self.y < 193 or 507 < self.y < 590):
                self.y -= self.speed
            if (98 < self.x < 184 or 738 < self.x < 822) and (382 < self.y < 630):
                self.y -= self.speed
            if 258 < self.x < 666 and 265 < self.y < 430:
                self.y -= self.speed

        if key[self.keyUp] and self.y > 30:
            self.rect.y -= self.speed
            self.y -= self.speed
            self.position = 3
            self.imgNum += 1
            if 98 < self.x < 822 and (105 < self.y < 193 or 507 < self.y < 590):
                self.y += self.speed
            if (98 < self.x < 184 or 738 < self.x < 822) and (107 < self.y < 310):
                self.y += self.speed
            if 258 < self.x < 666 and 265 < self.y < 430:
                self.y += self.speed

        if key[self.keyLeft] and self.x > 0:
            self.rect.x -= self.speed
            self.x -= self.speed
            self.position = 2
            self.imgNum += 1
            if (144 < self.x < 183 or 734 < self.x < 822) and (107 < self.y < 310 or 385 < self.y < 590):
                self.x += self.speed
            if 304 < self.x < 666 and 265 < self.y < 430:
                self.x += self.speed

        if key[self.keyRight] and self.x < 952:
            self.rect.x += self.speed
            self.x += self.speed
            self.position = 0
            self.imgNum += 1
            if (98 < self.x < 183 or 734 < self.x < 822) and (107 < self.y < 310 or 385 < self.y < 590):
                self.x -= self.speed
            if 258 < self.x < 666 and 265 < self.y < 430:
                self.x -= self.speed
        if key[self.keyShoot] and self.timeNull == 0 and self.timeLimit == 0:
            Bullets(self, self.x, self.y, self.position, self.bulradius, self.bulcolour, self.bulspeed, self.buldam)
            self.timeLimit = 10
            self.i += 1
            if self.i == 20:
                self.timeNull = 60
        if self.timeNull > 0:
            self.timeNull -= 1
            self.i = 0
        if self.timeLimit > 0:
            self.timeLimit -= 2
        if self.imgNum >= 6:
            self.imgNum = 0

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)
            self.hp = 0
            print(self.school + ' dead')

    def draw(self):
        window.windows.blit(self.image, (self.x, self.y))
        if len(objects) < 2:
            res_font = pygame.font.SysFont(None, 200)
            res = res_font.render(self.school + ' ' + 'WIN', True, 'aqua')
            res2 = res_font.render(self.school + ' ' + 'WIN', True, 'black')
            window.windows.blit(res2, res2.get_rect(center=(window.length / 2 + 3, window.width / 2 + 3)))
            window.windows.blit(res, res.get_rect(center=(window.length / 2, window.width / 2)))
        self.results()

    def results(self):
        j = 0
        result_font = pygame.font.SysFont(None, 35)
        for obj in objects:
            result = result_font.render(obj.school + ': ' + str(obj.hp), True, obj.bulcolour)
            window.windows.blit(result, (50 + j * 50, 3))
            j += 16

class Bullets():
    def __init__(self, parent, x, y, position, radius, colour, speed, damage):
        bullets.append(self)

        self.x, self.y = x + 24, y + 24
        self.px, self.py = x, y
        self.position = position
        self.radius = radius
        self.colour = colour
        self.speed = speed
        self.parent = parent
        self.damage = damage

    def moveSh(self):
        if self.position == 0:
            self.x += self.speed
            self.x += self.speed
        if self.position == 1:
            self.y += self.speed
        if self.position == 2:
            self.x -= self.speed
        if self.position == 3:
            self.y -= self.speed
            self.y -= self.speed
        if 306 <= self.x <= 664 and 313 <= self.y <= 431:
            bullets.remove(self)
        if 184 <= self.x <= 782 and (153 <= self.y <= 192 or 554 <= self.y <= 590):
            bullets.remove(self)
        if (144 <= self.x <= 153 or 782 <= self.x <= 822) and \
                (153 <= self.y <= 314 or 433 <= self.y <= 592):
            bullets.remove(self)
        if self.x <= 0 or self.x > window.length or self.y <= 30 or self.y > window.width:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.rect.collidepoint(self.x, self.y):
                    obj.damage(self.damage)
                    bullets.remove(self)
                    break

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def drawSh(self):
        pygame.draw.circle(window.windows, self.colour, (self.x, self.y), self.radius)
