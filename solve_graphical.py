import pygame
from pygame.locals import *
import sys
import time

import solve

sys.setrecursionlimit(10000)

maze = solve.MazeSolver(45, 45, 'wide')

SCREEN_SIZE = 800
cell_size_w = 800 / maze.maze_instance.width
cell_size_h = 800 / maze.maze_instance.height

pygame.init()  # 初期化
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))  # ウィンドウサイズの指定
pygame.display.set_caption("穴掘り法: 幅優先探索")  # ウィンドウの上の方に出てくるアレの指定

screen.fill((0, 0, 0,))  # 背景色の指定。RGBだと思う

f = maze.maze

for i in range(maze.maze_instance.height):
    for j in range(maze.maze_instance.width):
        if f[i][j] == 0:
            pygame.draw.rect(screen, (255, 255, 255),
                             Rect(i * cell_size_h, j * cell_size_w, cell_size_h + 1, cell_size_w + 1))
        elif f[i][j] == 2:
            pygame.draw.rect(screen, (0, 255, 0),
                             Rect(i * cell_size_h, j * cell_size_w, cell_size_h + 1, cell_size_w + 1))
        elif f[i][j] == 3:
            pygame.draw.rect(screen, (255, 0, 0),
                             Rect(i * cell_size_h, j * cell_size_w, cell_size_h + 1, cell_size_w + 1))

for i in maze.answer:
    if i != maze.start and i != maze.goal:
        pygame.draw.rect(screen, (0, 0, 255),
                         Rect(i[1] * cell_size_h, i[0] * cell_size_w, cell_size_h + 1, cell_size_w + 1))

pygame.display.update()  # 画面更新

while True:
    time.sleep(0.1)
    for event in pygame.event.get():  # 終了処理
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
