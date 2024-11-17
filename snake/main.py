import pygame
from pygame.locals import *

import game
import menu

pygame.init()

window = pygame.display.set_mode((500, 500))
difficulty = "medium"
print('bouh')
while True:
    difficulty = menu.start_menu(window, difficulty)
    game.game(window, difficulty)