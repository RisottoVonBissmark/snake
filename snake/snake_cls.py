import pygame
from pygame.locals import *

class Segment():

    def __init__(self, pos:list[int]|tuple[int], size: int, dir: str, color= "#22CC11")-> None:
        """
        create a snake segment object
        """

        self.rect = pygame.Rect(pos, (size, size))
        self.dir = dir
        self.color = color
        self.pos = pos

    def get_pos(self)-> object:
        """
        return the current position of the snake segment
        """
        return pygame.Vector2(self.rect.x, self.rect.y)
    
    def get_dir(self)-> str:
        """
        return the current direction of the snake segment
        """
        return self.dir
    
class Snake():

    def __init__(self, size: int)-> None:
        """
        create a snake object
        """
        
        self.score = 0

        self.dir = "r"
        self.length = 1
        self.segments = [Segment([0,0], size, self.dir, color="#229911")]
        self.size = size
        self.speed = 1

        self.moves = []
        self.game_over = False

    def move(self)-> None:
        """
        update the segments position
        """
        
        if len(self.moves) > 2:
            self.moves = self.moves[:1]
        
        #make every snake segment move
        i = self.length-1
        while i >= 0:
            segment = self.segments[i]

            if segment.dir == "r": 
                segment.rect.move_ip(self.speed, 0)

            if segment.dir == "l": 
                segment.rect.move_ip(-self.speed, 0)
            
            if segment.dir == "u": 
                segment.rect.move_ip(0, -self.speed)
            
            if segment.dir == "d":
                segment.rect.move_ip(0, self.speed)

            #make the segment rotate when its on a case
            if segment.get_pos().x % 25 == 0 and segment.get_pos().y % 25 == 0:
                
                if len(self.moves) > 0 and i == 0:
                    segment.dir = self.moves[0]
                    self.moves.pop(0)
                    self.dir = segment.dir

                if i != 0:
                    segment.dir = self.segments[i-1].get_dir()
            
            self.segments[i] = segment
            i -= 1

    def collision(self, height: int, length: int)-> None:
        """
        for collision with the snake an the window border
        """
        head = self.segments[0]
        for i in range(len(self.segments[2:])):
            if head.rect.colliderect(self.segments[2:][i].rect):
                self.game_over = True
        
        if head.rect.x < 0 or head.rect.x > length-self.size:
            self.game_over = True
        if head.rect.y < 0 or head.rect.y > height-self.size:
            self.game_over = True
    
    def grow(self):
        """
        create a new segment at the end of the snake
        """
        
        segment = self.segments[-1]
        
        pos = segment.get_pos()

        if segment.get_dir() == "r":
            pos.x -= self.size

        if segment.get_dir() == "l":
            pos.x += self.size
        
        if segment.get_dir() == "u":
            pos.y += self.size
        
        if segment.get_dir() == "d":
            pos.y -= self.size
        
        self.segments.append(
            Segment((pos.x, pos.y), self.size, segment.get_dir())
            )
        
        self.length += 1

    def draw(self, window:pygame.surface)-> None:
        """
        draw all snake segment on the surface
        """
        
        for i in range(self.length):
            segment = self.segments[i]
            pygame.draw.rect(window, segment.color, segment.rect)
