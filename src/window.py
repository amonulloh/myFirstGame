# This Class for Window

import pygame
pygame.init()


class Window:
    """
    This class responsible for size (length and
     width) of the display
    It is automatically run when you run "main.py", it
     will be imported into "mygame.py" and "player.py"
    """
    length = 1000
    width = 730
    windows = pygame.display.set_mode((length, width))
