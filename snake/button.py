import pygame
from pygame.locals import *

class Button():

    def __init__(self, texture: pygame.Surface, pos: list[int]|tuple[int], scale = 1) -> None:
        
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(
            self.texture, 
            [self.texture.get_width() * scale, self.texture.get_height() * scale]
        )
        self.rect = self.texture.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.pos = pos

        self.show = True

    def is_clicked(self):

        pygame.event.get()
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            if pygame.mouse.get_pressed()[0]:
                return True
            else:
                return False
        else:
            return False
    
    def draw(self, surface: pygame.Surface):
        if self.show:
            surface.blit(self.texture, self.pos)

    def hide(self):
        self.show = False
    
    def show(self):
        self.show = True