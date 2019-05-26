import solve
import pygame
from pygame.locals import *
import sys

sys.setrecursionlimit(10000)

maze = solve.MazeSolver(15, 15, 'deep')

SCREEN_SIZE = 800
cell_size_w = 800 / maze.maze_instance.width
cell_size_h = 800 / maze.maze_instance.height

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("穴掘り法: 幅優先探索")
c = pygame.time.Clock()

c_count = 0
s_count = 0

while True:
    c.tick(60)
    screen.fill((0, 0, 0,))

    c_cells = maze.maze_instance.diged_cells[:c_count]
    for i in c_cells:
        if maze.maze[i[1]][i[0]] != 2 and maze.maze[i[1]][i[0]] != 3:
            pygame.draw.rect(screen, (255, 255, 255),
                             Rect(i[1] * cell_size_h, i[0] * cell_size_w, cell_size_h + 1, cell_size_w + 1))
        elif maze.maze[i[1]][i[0]] == 2:
            pygame.draw.rect(screen, (0, 255, 0),
                             Rect(i[1] * cell_size_h, i[0] * cell_size_w, cell_size_h + 1, cell_size_w + 1))
        elif maze.maze[i[1]][i[0]] == 3:
            pygame.draw.rect(screen, (255, 0, 0),
                             Rect(i[1] * cell_size_h, i[0] * cell_size_w, cell_size_h + 1, cell_size_w + 1))
    if maze.goal not in c_cells:
        c_count += 1
    else:
        s_cells = maze.close[:s_count]
        for i in s_cells:
            if maze.maze[i[1]][i[0]] != 2 and maze.maze[i[1]][i[0]] != 3:
                pygame.draw.rect(screen, (178, 208, 255),
                                 Rect(i[1] * cell_size_h, i[0] * cell_size_w, cell_size_h + 1, cell_size_w + 1))
        if maze.goal not in s_cells:
            s_count += 1
        else:
            for i in maze.answer:
                if maze.maze[i[1]][i[0]] != 2 and maze.maze[i[1]][i[0]] != 3:
                    pygame.draw.rect(screen, (0, 0, 255),
                                     Rect(i[1] * cell_size_h, i[0] * cell_size_w, cell_size_h + 1, cell_size_w + 1))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
