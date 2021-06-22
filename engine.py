# -*- coding: utf-8 -*-
import pygame
from pygame.draw import *
from pygame.image import *
from pygame.locals import *
import sys

GRID_SIZE = 32
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
black = (0, 0, 0)
white = (255, 255, 255)

def main():
    # init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("roguelike")
    font = pygame.font.Font(".\data\misaki_gothic.ttf", GRID_SIZE)

    player = font.render("＠", True, white)
    # mainLoop
    while(True):
        pygame.display.update()
        pygame.time.wait(30)
        screen.fill((0,0,0))
        
        # here your code!

        screen.blit(player, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        for event in pygame.event.get(): # end
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()