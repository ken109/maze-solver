import solve
import pygame
from pygame.locals import *
import sys

sys.setrecursionlimit(10000)

while True:
    try:
        width = int(input('width:'))
        height = int(input('height:'))
        if width % 2 == 1 and height % 2 == 1:
            break
        else:
            print('奇数の整数値を入力してください')
    except ValueError:
        print('奇数の整数値を入力してください')

while True:
    mode = input('deep or wide:')
    if mode in ['deep', 'wide', 'a_star']:
        break
    else:
        print('deepかwideを入力してください')

maze = solve.MazeSolver(width, height, mode)

SCREEN_SIZE = 800
cell_size_w = 800 / maze.maze_instance.width
cell_size_h = 800 / maze.maze_instance.height

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("穴掘り法: 幅優先探索")
c = pygame.time.Clock()

count = 0

while True:
    c.tick(10)
    screen.fill((0, 0, 0,))

    for i in range(maze.maze_instance.height):
        for j in range(maze.maze_instance.width):
            if maze.maze[i][j] == 0:
                pygame.draw.rect(screen, (255, 255, 255),
                                 Rect(i * cell_size_h, j * cell_size_w, cell_size_h + 1, cell_size_w + 1))
            elif maze.maze[i][j] == 2:
                pygame.draw.rect(screen, (0, 255, 0),
                                 Rect(i * cell_size_h, j * cell_size_w, cell_size_h + 1, cell_size_w + 1))
            elif maze.maze[i][j] == 3:
                pygame.draw.rect(screen, (255, 0, 0),
                                 Rect(i * cell_size_h, j * cell_size_w, cell_size_h + 1, cell_size_w + 1))

    close_cell = maze.close[:count]
    for i in close_cell:
        if maze.maze[i[1]][i[0]] != 2 and maze.maze[i[1]][i[0]] != 3:
            pygame.draw.rect(screen, (178, 208, 255),
                             Rect(i[1] * cell_size_h, i[0] * cell_size_w, cell_size_h + 1, cell_size_w + 1))

    if maze.goal not in close_cell:
        count += 1
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
