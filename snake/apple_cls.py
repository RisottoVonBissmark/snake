import pygame
from pygame.locals import *
import random

class Apple():

    def __init__(self, size, height, length)-> None:

        self.size = size
        self.pos_x = random.randint(0, (length//size)-1)*size
        self.pos_y = random.randint(0, (height//size)-1)*size
        
        self.rect = pygame.Rect(self.pos_x, self.pos_y, size, size)

        self.color = "#FF1111"
    
    def reset(self, height, length)-> None:
        self.pos_x = random.randint(0, (length//self.size)-1)*self.size
        self.pos_y = random.randint(0, (height//self.size)-1)*self.size
        
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.size, self.size)

    def draw(self, window)-> None:
        
        pygame.draw.rect(window, self.color, self.rect)
