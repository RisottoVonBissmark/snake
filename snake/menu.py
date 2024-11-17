import sys
import pygame
from pygame.locals import *

import button

class Menu():

    def __init__(self):
        
        self.buttons = []

    def update(self):
        pass

    def draw(self, surface: pygame.Surface):
        for i in range(len(self.buttons)):
            self.buttons[i].draw(surface)

class Start_Menu(Menu):

    def __init__(self):
        super().__init__()

        self.start_button = button.Button("img\\play_button.png", [50, 50], 10)
        self.dificulty_button = button.Button("img\\difficulty_button.png", [50, 200], 10)
        self.quit_button = button.Button("img\\quit_button.png", [50, 350], 10)
        
        self.buttons.append(self.start_button)
        self.buttons.append(self.dificulty_button)
        self.buttons.append(self.quit_button)

    def update(self):
        if self.start_button.is_clicked():
            return "start"

        if self.dificulty_button.is_clicked():
            return "dificulty"
        
        if self.quit_button.is_clicked():
            return "quit"
        
class Dificulty_Menu(Menu):

    def __init__(self):
        super().__init__()
    
        self.easy_button = button.Button("img\\easy_button.png", [50, 50], 10)
        self.medium_button = button.Button("img\\medium_button.png", [50, 200], 10)
        self.hard_button = button.Button("img\\hard_button.png", [50, 350], 10)

        self.buttons.append(self.easy_button)
        self.buttons.append(self.medium_button)
        self.buttons.append(self.hard_button)
    
    def update(self):
        
        if self.easy_button.is_clicked():
            return "easy"
        if self.medium_button.is_clicked():
            return "medium"
        if self.hard_button.is_clicked():
            return "hard"


def start_menu(window: pygame.Surface, dificulty):

    menu = Start_Menu()
    dificulty

    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.time.wait(250)

        menu_event = menu.update()

        if menu_event == "start":
            return dificulty
        if menu_event == "dificulty":
            menu = Dificulty_Menu()
        if menu_event == "easy":
            dificulty = "easy"
            menu = Start_Menu()
        if menu_event == "medium":
            dificulty = "medium"
            menu = Start_Menu()
        if menu_event == "hard":
            dificulty = "hard"
            menu = Start_Menu()
        if menu_event == "quit":
            pygame.quit()
            sys.exit()

        window.fill("#000000")
        menu.draw(window)

        pygame.display.update()