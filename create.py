import random


class MazeCreator:
    def __init__(self, width=45, height=45):
        self.width = width
        self.height = height
        self.start = [random.randrange(1, self.width, 2), random.randrange(1, self.height, 2)]
        self.last_cell = []
        self.maze = [[0 for i in range(self.width)] if j == 0 or j == self.height - 1
                     else [0 if i == 0 or i == self.width - 1 else 1 for i in range(self.width)] for j in
                     range(self.height)]
        self.start_cells = [[i, j] for i in range(1, self.width, 2) for j in range(1, self.height, 2)]
        self.start_cells.remove(self.start)
        self.dug_cells = [self.start]
        self.dig(self.start)

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
                for i in range(self.height):
                    for j in range(self.width):
                        if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
                            self.maze[i][j] = 1
                self.maze[self.start[1]][self.start[0]] = 2
                self.maze[self.last_cell[1]][self.last_cell[0]] = 3
            else:
                self.dig([next_cell[0], next_cell[1]])

    def obstacle(self):
        pass

    def get_cell(self):
        if len(self.start_cells) == 0:
            cell = None
        else:
            cell = random.choice(self.start_cells)
            while self.maze[cell[1]][cell[0]] != 0:
                cell = random.choice(self.start_cells)
            self.start_cells.remove(cell)
        return cell


def print_maze():
    m = MazeCreator(7, 7)
    for i in range(m.height):
        for j in range(m.width):
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
