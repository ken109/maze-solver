import create
import pygame
from pygame.locals import *
import sys
import time

maze = create.MazeCreator(45, 45)

SCREEN_SIZE = 800
cell_size = 800 / maze.width

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Test")

count = 0

while True:
    screen.fill((0, 0, 0,))

    draw_cells = maze.dug_cells[:count]

    for i in draw_cells:
        if maze.maze[i[1]][i[0]] != 2 and maze.maze[i[1]][i[0]] != 3:
            pygame.draw.rect(screen, (255, 255, 255),
                             Rect(i[0] * cell_size, i[1] * cell_size, cell_size + 1, cell_size + 1))
        if maze.maze[i[1]][i[0]] == 2:
            pygame.draw.rect(screen, (0, 255, 0),
                             Rect(i[0] * cell_size, i[1] * cell_size, cell_size + 1, cell_size + 1))
        if maze.maze[i[1]][i[0]] == 3:
            pygame.draw.rect(screen, (255, 0, 0),
                             Rect(i[0] * cell_size, i[1] * cell_size, cell_size + 1, cell_size + 1))

    pygame.display.update()
    if maze.last_cell not in draw_cells:
        count += 1

    time.sleep(0.01)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
