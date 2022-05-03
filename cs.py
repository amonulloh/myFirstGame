import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 20

pygame.display.set_caption("CS_2D")

image1 = [pygame.image.load('soldier11.png'), pygame.image.load('soldier11.png'), pygame.image.load('soldier11.png'),
        pygame.image.load('soldier12.png'), pygame.image.load('soldier12.png'), pygame.image.load('soldier12.png')]
image2 = [pygame.image.load('soldier21.png'), pygame.image.load('soldier21.png'), pygame.image.load('soldier21.png'),
        pygame.image.load('soldier22.png'), pygame.image.load('soldier22.png'), pygame.image.load('soldier22.png')]
map = pygame.image.load('map_cs.png')

class Gl:
        @staticmethod
        def play():
                pass

class player:
        def __init__(self):
                pass


