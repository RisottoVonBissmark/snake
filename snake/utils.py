import time
import math

class Timer():

    def __init__(self, delay: int|float) -> None:
        """
        create a timer
        """
        
        self.delay = delay
        self.launch_t = time.time()
    
    def is_ended(self)-> bool:
        """
        check if delay is ended
        """
        
        if time.time() - self.launch_t > self.delay:
            return True
        else:
            return False
    
    def reset(self)-> None:
        """
        reset the timer
        """

        self.launch_t = time.time()

def to_grid(snake, apple, dimension, scale):
    
    grid = [["0" for i in range(dimension[1])] for j in range(dimension[0])]
    
    for segment in snake.segments:
        
        pos = segment.get_pos()
        grid[int(pos.y) // scale][int(pos.x) // scale] = "1"
    
    grid[apple.pos_y // scale][apple.pos_y // scale] = "2"

    return grid

class Node():

    def __init__(self, pos, parent = None, g = 0, h = 0, dir = "u"):
        self.pos = pos
        self.parent = parent
        
        self.dir = dir
        self.g = g
        self.h = h
        self.f = self.g + self.h

class NoPathError(Exception):
    """
    ther is no path
    """
    pass

def path_finding(grid, start, end, wall):
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
        for new_pos in ([1,0, 10, "d"], [-1,0, 10, "u"], [0,1, 10, "l"], [0,-1, 10, "r"]): #, [1,1, 14], [1,-1, 14], [-1,-1, 14], [-1,1, 14]):
            
            pos = [currentNode.pos[0] + new_pos[0], currentNode.pos[1] + new_pos[1]]

            if pos[0] < 0 or pos[1] < 0 or pos[0] > len(grid)-1 or pos[1] > len(grid[0])-1:
                continue

            if grid[pos[0]][pos[1]] in wall:
                continue
            
            children.append(Node((pos[0], pos[1]), g = new_pos[2], dir=new_pos[3]))

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
    path_1 = []
    path_2 = []
    node = currentNode
    while node.pos != start:
        path_1.append(node.dir)
        path_2.append(node.pos)
        node = node.parent
    
    return (path_1, path_2)