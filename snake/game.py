import sys
#import A_star_pathfinding
import pygame
from pygame.locals import *

pygame.init()

import snake_cls
import apple_cls
import utils

def game(window, difficulty) -> int:

    print(difficulty)
    if difficulty == "hard":
        max_speed = 0.0005
        speed_boost = 0.90
    elif difficulty == "medium":
        max_speed = 0.001
        speed_boost = 0.925
    else:
        max_speed = 0.005
        speed_boost = 0.95

    
    snake = snake_cls.Snake(25)
    apple = apple_cls.Apple(25, 500, 500)
    
    move_timer = utils.Timer(0.01)
    last_key = ""

    while not snake.game_over:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        keydown = pygame.key.get_pressed()
        #print(snake.moves)
        if keydown[K_UP] and last_key != "u" and snake.dir != "d":
            snake.moves.append("u")
            last_key = "u"
        if keydown[K_DOWN] and last_key != "d" and snake.dir != "u":
            snake.moves.append("d")
            last_key = "d"
        if keydown[K_LEFT] and last_key != "l" and snake.dir != "r":
            snake.moves.append("l")
            last_key = "l"
        if keydown[K_RIGHT] and last_key != "r" and snake.dir != "l":
            snake.moves.append("r")
            last_key = "r"
            
        if move_timer.is_ended():
            snake.move()
            snake.collision(500, 500)
            move_timer.reset()
        
        if snake.segments[0].rect.colliderect(apple.rect):
            snake.score += 1

            snake.grow()
            apple.reset(500, 500)
            if move_timer.delay >= max_speed:
                move_timer.delay *= speed_boost

        window.fill("#000000")
        snake.draw(window)
        apple.draw(window)
        pygame.display.update()

    print(f"""
    -----------------------------
    votre score : {snake.score}
    -----------------------------
    """)

    return snake.score

