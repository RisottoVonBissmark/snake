"""
A* pathfinding algorithm
"""

import pygame
import math
import time
import random

from pygame.locals import *

pygame.init()

class Node():

    def __init__(self, pos, parent = None, g = 0, h = 0):
        self.pos = pos
        self.parent = parent
        
        self.g = g
        self.h = h
        self.f = self.g + self.h

class NoPathError(Exception):
    """
    ther is no path
    """
    pass

def A_star(lab: list[list[str]], start: tuple, end:tuple, wall:str) -> list :
    """
    find the fastest way from start to end
    """

    open = []       #nodes to explore    
    closed = []     #nodes already explored

    open.append(Node(start))

    end_reached = False
    while not end_reached:

        if len(open) == 0:
            raise NoPathError
        
        #get the node with the lower F
        min = open[0].f
        currentNodeIndex = 0
        for i in range(len(open)):
            if open[i].f == min:
                if open[i].h < open[currentNodeIndex].h:
                    currentNodeIndex = i
            if open[i].f < min:
                min = open[i].f
                currentNodeIndex = i

        currentNode = open[currentNodeIndex]
        closed.append(open.pop(currentNodeIndex).pos)

        #create childrens
        children = []
        for new_pos in ([1,0, 10], [-1,0, 10], [0,1, 10], [0,-1, 10]): #, [1,1, 14], [1,-1, 14], [-1,-1, 14], [-1,1, 14]):
            
            pos = [currentNode.pos[0] + new_pos[0], currentNode.pos[1] + new_pos[1]]

            if pos[0] < 0 or pos[1] < 0 or pos[0] > len(lab)-1 or pos[1] > len(lab[0])-1:
                continue

            if lab[pos[0]][pos[1]] in wall:
                continue
            
            children.append(Node((pos[0], pos[1]), g = new_pos[2]))

        for child in children:

            #check if child already used
            if child.pos in closed:
                continue
            
            child.parent = currentNode
            child.g += currentNode.g
            child.h = int(round(math.sqrt((child.pos[0] - end[0])**2 + (child.pos[1] - end[1])**2), 2) * 10)    #distance from end (pythagor)
            child.f = child.g + child.h

            if child.pos[0] == end[0] and child.pos[1] == end[1]:
                end_reached = True

            for node in open:
                if child.pos == node.pos:
                    if child.g > node.g:
                        continue
                    else:
                        closed.append(open.pop(open.index(node)).pos)
            
            open.append(child)

    #get path
    path = []
    node = currentNode
    while node.pos != start:
        path.append(node.pos)
        node = node.parent
    
    return path



def graphical_A_star(lab: list[list[str]], start: tuple, end:tuple, wall:str, t_size = 16) -> list :
    """
    find the fastest way from start to end
    """

    #create pygame window
    window = pygame.display.set_mode((len(lab)*t_size, len(lab[0])*t_size))

    open = []       #nodes to explore    
    closed = []     #nodes already explored

    open.append(Node(start))
    
    tile = pygame.Surface((t_size,t_size))
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] in wall:
                tile.fill('#000000')
            else:
                tile.fill('#FFFFFF')
            window.blit(tile, (j*t_size, i*t_size))
    pygame.display.update()
    time.sleep(3)

    end_reached = False
    count = 0
    while not end_reached:

        if len(open) == 0:
            raise NoPathError
        
        #get the node with the lower F
        min = open[0].f
        currentNodeIndex = 0
        for i in range(len(open)):
            if open[i].f == min:
                if open[i].h < open[currentNodeIndex].h:
                    currentNodeIndex = i
            if open[i].f < min:
                min = open[i].f
                currentNodeIndex = i

        currentNode = open[currentNodeIndex]
        closed.append(open.pop(currentNodeIndex).pos)

        if currentNode.pos[0] == end[0] and currentNode.pos[1] == end[1]:
            end_reached = True

        #create childrens
        children = []
        for new_pos in ([1,0, 10], [-1,0, 10], [0,1, 10], [0,-1, 10], [1,1, 14], [1,-1, 14], [-1,-1, 14], [-1,1, 14]):
            
            pos = [currentNode.pos[0] + new_pos[0], currentNode.pos[1] + new_pos[1]]

            if pos[0] < 0 or pos[1] < 0 or pos[0] > len(lab)-1 or pos[1] > len(lab[0])-1:
                continue

            if lab[pos[0]][pos[1]] in wall:
                continue
            
            children.append(Node((pos[0], pos[1]), g = new_pos[2]))

        for child in children:

            #check if child already used
            if child.pos in closed:
                continue
            
            child.parent = currentNode
            child.g += currentNode.g
            child.h = int(round(math.sqrt((child.pos[0] - end[0])**2 + (child.pos[1] - end[1])**2), 2) * 10)    #distance from end (pythagor)
            child.f = child.g + child.h

            for node in open:
                if child.pos == node.pos:
                    if child.g > node.g:
                        continue
                    else:
                        closed.append(open.pop(open.index(node)).pos)
            
            open.append(child)
        
        tile.fill('#00AA00')
        for i in open:
            window.blit(tile, (i.pos[1]*t_size, i.pos[0]*t_size))

        tile.fill('#AA0000')
        for i in closed:
            window.blit(tile, (i[1]*t_size, i[0]*t_size))

        pygame.display.update()
        
        """
        pygame.event.get()
        key = pygame.key.get_pressed()
        while not key[pygame.K_a]:
            pygame.event.get()
            key = pygame.key.get_pressed()
        """
        count += 1
        #print(count)
        time.sleep(0.01)

    
    #get path
    path = []
    node = currentNode
    tile.fill('#0000AA')
    while node.pos != start:
        
        path.append(node.pos)
        node = node.parent

        window.blit(tile, (node.pos[1]*t_size, node.pos[0]*t_size))
        pygame.display.update()
        """
        pygame.event.get()
        key = pygame.key.get_pressed()
        while not key[pygame.K_a]:
            pygame.event.get()
            key = pygame.key.get_pressed()
        """
        time.sleep(0.01)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


def path_tracing(lab:list, wall:list|str, *points):

    lpoints = []
    for i in range(len(points)):
        lpoints.append(points[i])
    
    path = []
    while len(lpoints) > 1:
        start = lpoints.pop(0)
        print(lpoints)
        print(start)
        print(lpoints[0])
        path += A_star(lab, start, lpoints[0], wall)

        print("ok")
    return path

def lab_gen():

    lab = [[' ' for i in range(100)] for j in range(100)]
    start = [0,0]
    end = [99,99]
    wall = '#'

    #create checkpoints
    checkpoints = []
    checkpoints.append(start)
    for i in range(random.randint(0, 10)):
        checkpoints.append([random.randint(0, 99), random.randint(0, 99)])
    
    checkpoints.append(end)

    #create path
    path = []
    path += checkpoints

    while len(checkpoints) > 1:
        start = checkpoints.pop(0)
        path += A_star(lab, start, checkpoints[0], wall)

    for i in range(len(path)):
        if type(path[i]) == type([]):
            path[i] = (path[i][0], path[i][1])

    #create lab
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if (j,i) in path:
                continue

            lab[i][j] = random.choices([' ','#'], [2, 3])[0]
    
    return(lab)

lab = [
    [' ','#',' ',' ',' ',' ',' ','#','#',' '],
    [' ','#','#','#','#',' ',' ',' ',' ',' '],
    [' ','#',' ','#',' ',' ','#',' ','#',' '],
    [' ',' ',' ','#',' ',' ',' ',' ','#',' '],
    [' ','#',' ','#',' ',' ','#',' ','#',' '],
    [' ','#','#','#',' ',' ','#',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ','#',' ',' ',' '],
    [' ','#','#','#',' ','#','#','#','#',' '],
    [' ',' ',' ','#',' ',' ','#',' ',' ',' '],
    [' ','#',' ',' ',' ',' ','#',' ',' ','#']
]

#lab = lab_gen()


print(f"size : {int(len(lab))*len(lab[0])}")

path = graphical_A_star(lab, (0,0), (9, 8), '#', 32)

"""
t_0 = time.time()
path = A_star(lab,[0,0], [99,99],"#")
t_1 = time.time()

print(f"executed in {t_1-t_0} secondes")


for i in range(len(path)):
    lab[path[i][0]][path[i][1]] = 'X'


for i in range(len(lab)):
    print(lab[i])
"""