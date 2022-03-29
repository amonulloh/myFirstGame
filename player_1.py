#This Class for Player_1
import pygame
import window


class Player():
    def __init__(self, x, y, radius, colour, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.colour = colour

    def move(self, *args):
        """
        в args надо передавать клавиши отвечающие за передвижение в порядке
        вверх, вниз, влево, вправо
        """
        key = pygame.key.get_pressed()
        if key[args[2]] and self.x > 5 + self.radius:
            self.x -= self.speed
        if key[args[3]] and self.x < 995 - self.radius:
            self.x += self.speed
        if key[args[0]] and self.y > 5 + self.radius:
            self.y -= self.speed
        if key[args[1]] and self.y < 495 - self.radius:
            self.y += self.speed

    def draw(self):
        pygame.draw.circle(window.windows, self.colour, (self.x, self.y), self.radius)
