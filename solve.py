import create


class MazeSolver:
    def __init__(self, width=45, height=45, mode='wide'):
        self.maze_instance = create.MazeCreator(width, height)
        self.maze = self.maze_instance.maze
        self.start = self.maze_instance.start
        self.goal = self.maze_instance.last_cell
        self.pointer = []
        self.open = []
        self.a_open = []
        self.close = []
        self.answer = []
        if mode == 'wide':
            self.open.append(self.start)
            self.wide()
        elif mode == 'deep':
            self.open.append(self.start)
            self.deep()
        elif mode == 'a_star':
            self.a_open.append([self.start, [0, self.get_cost(self.start)]])
            self.a_star()

    def wide(self):
        # オープンリストに要素があるなら取り出す
        if len(self.open) > 0:
            node = self.open[0]
            # 取り出したノードがゴールで終了
            if node == self.goal:
                self.answer_pointer(self.goal)
            self.close.append(node)
            self.open.remove(node)
            # 方向
            if self.maze[node[1] - 1][node[0]] == 0 or self.maze[node[1] - 1][node[0]] == 3:  # 上
                if not [node[0], node[1] - 1] in self.close:
                    self.open.append([node[0], node[1] - 1])
                    self.pointer.append([[node[0], node[1]], [node[0], node[1] - 1]])
            if self.maze[node[1]][node[0] + 1] == 0 or self.maze[node[1]][node[0] + 1] == 3:  # 右
                if not [node[0] + 1, node[1]] in self.close:
                    self.open.append([node[0] + 1, node[1]])
                    self.pointer.append([[node[0], node[1]], [node[0] + 1, node[1]]])
            if self.maze[node[1] + 1][node[0]] == 0 or self.maze[node[1] + 1][node[0]] == 3:  # 下
                if not [node[0], node[1] + 1] in self.close:
                    self.open.append([node[0], node[1] + 1])
                    self.pointer.append([[node[0], node[1]], [node[0], node[1] + 1]])
            if self.maze[node[1]][node[0] - 1] == 0 or self.maze[node[1]][node[0] - 1] == 3:  # 左
                if not [node[0] - 1, node[1]] in self.close:
                    self.open.append([node[0] - 1, node[1]])
                    self.pointer.append([[node[0], node[1]], [node[0] - 1, node[1]]])
            self.wide()

    def deep(self):
        # オープンリストに要素があるなら取り出す
        if len(self.open) > 0:
            node = self.open[-1]
            # 取り出したノードがゴールで終了
            if node == self.goal:
                self.answer_pointer(self.goal)
            self.close.append(node)
            self.open.remove(node)
            # 方向
            if self.maze[node[1] - 1][node[0]] == 0 or self.maze[node[1] - 1][node[0]] == 3:  # 上
                if not [node[0], node[1] - 1] in self.close:
                    self.open.append([node[0], node[1] - 1])
                    self.pointer.append([[node[0], node[1]], [node[0], node[1] - 1]])
            if self.maze[node[1]][node[0] + 1] == 0 or self.maze[node[1]][node[0] + 1] == 3:  # 右
                if not [node[0] + 1, node[1]] in self.close:
                    self.open.append([node[0] + 1, node[1]])
                    self.pointer.append([[node[0], node[1]], [node[0] + 1, node[1]]])
            if self.maze[node[1] + 1][node[0]] == 0 or self.maze[node[1] + 1][node[0]] == 3:  # 下
                if not [node[0], node[1] + 1] in self.close:
                    self.open.append([node[0], node[1] + 1])
                    self.pointer.append([[node[0], node[1]], [node[0], node[1] + 1]])
            if self.maze[node[1]][node[0] - 1] == 0 or self.maze[node[1]][node[0] - 1] == 3:  # 左
                if not [node[0] - 1, node[1]] in self.close:
                    self.open.append([node[0] - 1, node[1]])
                    self.pointer.append([[node[0], node[1]], [node[0] - 1, node[1]]])
            self.deep()

    def a_star(self):
        # オープンリストに要素があるなら取り出す
        if len(self.a_open) > 0:
            node = self.node_choice()  # [[x, y], [a, b]]
            n_cell = node[0]  # [x, y]
            n_cost = node[1]  # [a, b]
            # 取り出したノードがゴールで終了
            if node[0] == self.goal:
                self.answer_pointer(self.goal)

            self.close.append(node[0])
            self.a_open.remove(node)

            if self.maze[n_cell[1] - 1][n_cell[0]] == 0 or self.maze[n_cell[1] - 1][n_cell[0]] == 3:  # 上
                if not [n_cell[0], n_cell[1] - 1] in self.close:
                    self.a_open.append([[n_cell[0], n_cell[1] - 1], [n_cost[0] + 1, self.get_cost(n_cell)]])
                    self.pointer.append([[n_cell[0], n_cell[1]], [n_cell[0], n_cell[1] - 1]])
            if self.maze[n_cell[1]][n_cell[0] + 1] == 0 or self.maze[n_cell[1]][n_cell[0] + 1] == 3:  # 右
                if not [n_cell[0] + 1, n_cell[1]] in self.close:
                    self.a_open.append([[n_cell[0] + 1, n_cell[1]], [n_cost[0] + 1, self.get_cost(n_cell)]])
                    self.pointer.append([[n_cell[0], n_cell[1]], [n_cell[0] + 1, n_cell[1]]])
            if self.maze[n_cell[1] + 1][n_cell[0]] == 0 or self.maze[n_cell[1] + 1][n_cell[0]] == 3:  # 下
                if not [n_cell[0], n_cell[1] + 1] in self.close:
                    self.a_open.append([[n_cell[0], n_cell[1] + 1], [n_cost[0] + 1, self.get_cost(n_cell)]])
                    self.pointer.append([[n_cell[0], n_cell[1]], [n_cell[0], n_cell[1] + 1]])
            if self.maze[n_cell[1]][n_cell[0] - 1] == 0 or self.maze[n_cell[1]][n_cell[0] - 1] == 3:  # 左
                if not [n_cell[0] - 1, n_cell[1]] in self.close:
                    self.a_open.append([[n_cell[0] - 1, n_cell[1]], [n_cost[0] + 1, self.get_cost(n_cell)]])
                    self.pointer.append([[n_cell[0], n_cell[1]], [n_cell[0] - 1, n_cell[1]]])
            self.a_star()

    def get_cost(self, cell):
        # ゴールへの予想コストをreturn
        return abs(self.goal[0] - cell[0]) + abs(self.goal[1] - cell[1])

    def node_choice(self):
        # return [[x, y], [a, b]]
        sum_min = [self.a_open[0]]
        node = self.a_open[0]
        for i in self.a_open:
            if node[1][0] + node[1][1] > i[1][0] + i[1][1]:
                node = i
            elif node[1][0] + node[1][1] == i[1][0] + i[1][1] and node[0][0] + node[0][1] != i[0][0] + i[0][1]:
                sum_min.append(i)
        if len(sum_min) == 1:
            return node
        else:
            st_max = [sum_min[0]]
            node = sum_min[0]
            for i in sum_min:
                if node[1][0] + node[1][1] < i[1][0] + i[1][1]:
                    node = i
                elif node[1][0] + node[1][1] == i[1][0] + i[1][1] and node[0][0] + node[0][1] != i[0][0] + i[0][1]:
                    st_max.append(i)
            if len(st_max) == 1:
                return node
            else:
                node = st_max[0]
                return node

    def answer_pointer(self, cell):
        for i in self.pointer:
            if i[1] == cell:
                self.answer.insert(0, i[1])
                if i[0] != self.start:
                    self.answer_pointer(i[0])
                else:
                    self.answer.insert(0, i[0])


if __name__ == '__main__':
    m = MazeSolver(9, 9, 'a_star')
    print(m.maze)
    print(m.close)
    print(m.answer)
