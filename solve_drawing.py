import sys

import pygame
from pygame.locals import *

import solve

sys.setrecursionlimit(10000)

maze = solve.MazeSolver.new()

SCREEN_SIZE = 800

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
if maze.mode == 'wide':
    pygame.display.set_caption("穴掘り法: 幅優先探索")
elif maze.mode == 'deep':
    pygame.display.set_caption("穴掘り法: 深さ優先探索")
elif maze.mode == 'a_star':
    pygame.display.set_caption("穴掘り法: a*アルゴリズム")

while True:
    pygame.time.Clock().tick(60)

    maze.draw_cells(screen, SCREEN_SIZE)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
