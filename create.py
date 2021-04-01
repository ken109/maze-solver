import random
import time

import pygame
from pygame.locals import *


class MazeCreator:
    draw_count = 0

    def __init__(self, column=45, row=45):
        self.column = column
        self.row = row
        self.start = [random.randrange(1, self.column, 2), random.randrange(1, self.row, 2)]
        self.last_cell = []
        self.maze = [[0 for i in range(self.column)] if j == 0 or j == self.row - 1
                     else [0 if i == 0 or i == self.column - 1 else 1 for i in range(self.column)] for j in
                     range(self.row)]
        self.start_cells = [[i, j] for i in range(1, self.column, 2) for j in range(1, self.row, 2)]
        self.start_cells.remove(self.start)
        self.dug_cells = [self.start]
        self.dig(self.start)

    @classmethod
    def new(cls):
        message = '奇数の整数値を入力してください'
        while True:
            try:
                column = int(input('column: '))
                row = int(input('row: '))
                if column % 2 == 1 and row % 2 == 1:
                    break
                else:
                    print(message)
            except ValueError:
                print(message)
        return cls(column, row)

    def dig(self, cell):

        # 基準点を通路に
        self.maze[cell[1]][cell[0]] = 0

        # 進める方向をリストに格納
        directions = []
        if self.maze[cell[1] + 1][cell[0]] == 1 and self.maze[cell[1] + 2][cell[0]] == 1:
            directions.append('down')
        if self.maze[cell[1] - 1][cell[0]] == 1 and self.maze[cell[1] - 2][cell[0]] == 1:
            directions.append('up')
        if self.maze[cell[1]][cell[0] + 1] == 1 and self.maze[cell[1]][cell[0] + 2] == 1:
            directions.append('right')
        if self.maze[cell[1]][cell[0] - 1] == 1 and self.maze[cell[1]][cell[0] - 2] == 1:
            directions.append('left')

        # 掘っていく
        if len(directions) != 0:
            direction = random.choice(directions)
            if direction == 'down':
                self.maze[cell[1] + 1][cell[0]] = 0
                self.maze[cell[1] + 2][cell[0]] = 0
                self.last_cell = [cell[0], cell[1] + 2]
                self.dug_cells.append([cell[0], cell[1] + 1])
                self.dug_cells.append([cell[0], cell[1] + 2])
                self.dig([cell[0], cell[1] + 2])
            elif direction == 'up':
                self.maze[cell[1] - 1][cell[0]] = 0
                self.maze[cell[1] - 2][cell[0]] = 0
                self.last_cell = [cell[0], cell[1] - 2]
                self.dug_cells.append([cell[0], cell[1] - 1])
                self.dug_cells.append([cell[0], cell[1] - 2])
                self.dig([cell[0], cell[1] - 2])
            elif direction == 'right':
                self.maze[cell[1]][cell[0] + 1] = 0
                self.maze[cell[1]][cell[0] + 2] = 0
                self.last_cell = [cell[0] + 2, cell[1]]
                self.dug_cells.append([cell[0] + 1, cell[1]])
                self.dug_cells.append([cell[0] + 2, cell[1]])
                self.dig([cell[0] + 2, cell[1]])
            elif direction == 'left':
                self.maze[cell[1]][cell[0] - 1] = 0
                self.maze[cell[1]][cell[0] - 2] = 0
                self.last_cell = [cell[0] - 2, cell[1]]
                self.dug_cells.append([cell[0] - 1, cell[1]])
                self.dug_cells.append([cell[0] - 2, cell[1]])
                self.dig([cell[0] - 2, cell[1]])
        else:
            next_cell = self.get_cell()
            if next_cell is None:
                for i in range(self.row):
                    for j in range(self.column):
                        if i == 0 or i == self.row - 1 or j == 0 or j == self.column - 1:
                            self.maze[i][j] = 1
                self.maze[self.start[1]][self.start[0]] = 2
                self.maze[self.last_cell[1]][self.last_cell[0]] = 3
            else:
                self.dig([next_cell[0], next_cell[1]])

    def get_cell(self):
        if len(self.start_cells) == 0:
            cell = None
        else:
            cell = random.choice(self.start_cells)
            while self.maze[cell[1]][cell[0]] != 0:
                cell = random.choice(self.start_cells)
            self.start_cells.remove(cell)
        return cell

    def draw_cells(self, screen, screen_size, delay: bool = True) -> bool:
        cell_size = sum((screen_size / self.column, screen_size / self.row)) / 2

        screen.fill((0, 0, 0))

        draw_cells = self.dug_cells[:self.draw_count] if delay else self.dug_cells

        for i in draw_cells:
            if self.maze[i[1]][i[0]] != 2 and self.maze[i[1]][i[0]] != 3:
                pygame.draw.rect(screen, (255, 255, 255),
                                 Rect(i[0] * cell_size, i[1] * cell_size, cell_size + 1, cell_size + 1))
            if self.maze[i[1]][i[0]] == 2:
                pygame.draw.rect(screen, (0, 255, 0),
                                 Rect(i[0] * cell_size, i[1] * cell_size, cell_size + 1, cell_size + 1))
            if self.maze[i[1]][i[0]] == 3:
                pygame.draw.rect(screen, (255, 0, 0),
                                 Rect(i[0] * cell_size, i[1] * cell_size, cell_size + 1, cell_size + 1))

        time.sleep(0.01)

        if self.last_cell not in draw_cells:
            self.draw_count += 1
            return False
        else:
            return True


def print_maze():
    m = MazeCreator(7, 7)
    for i in range(m.row):
        for j in range(m.column):
            if m.maze[i][j] == 0:
                print('.', end='')
            elif m.maze[i][j] == 1:
                print('0', end='')
            elif m.maze[i][j] == 2:
                print('s', end='')
            elif m.maze[i][j] == 3:
                print('g', end='')
        print(' ')


if __name__ == '__main__':
    print_maze()
