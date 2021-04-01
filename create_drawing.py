import sys

import pygame
from pygame.locals import *

import create

maze = create.MazeCreator.new()

SCREEN_SIZE = 800

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Create")

while True:
    pygame.time.Clock().tick(60)

    maze.draw_cells(screen, SCREEN_SIZE)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
