import pygame
from pygame.locals import *
import sys
import time

import create

maze = create.MazeCreator(25, 25)

cell_size = 20
screen_width = cell_size * maze.width
screen_height = cell_size * maze.height

pygame.init()  # 初期化
screen = pygame.display.set_mode((screen_width, screen_height))  # ウィンドウサイズの指定
pygame.display.set_caption("穴掘り法")  # ウィンドウの上の方に出てくるアレの指定

screen.fill((0, 0, 0,))  # 背景色の指定。RGBだと思う

f = maze.maze

for i in range(maze.height):
    for j in range(maze.width):
        if f[i][j] == 0:
            pygame.draw.rect(screen, (255, 255, 255), Rect(j * cell_size, i * cell_size, cell_size, cell_size))
        elif f[i][j] == 2:
            pygame.draw.rect(screen, (0, 255, 0), Rect(j * cell_size, i * cell_size, cell_size, cell_size))
        elif f[i][j] == 3:
            pygame.draw.rect(screen, (255, 0, 0), Rect(j * cell_size, i * cell_size, cell_size, cell_size))

pygame.display.update()  # 画面更新

while True:
    time.sleep(0.1)
    for event in pygame.event.get():  # 終了処理
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
