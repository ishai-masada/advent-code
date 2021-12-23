from pprint import pprint

# Day 4
# Bingo
# Ishai Masada


class Board:
    def __init__(self, rows):
        self.rows = rows

    def row(self, row_index):
        return self.rows[row_index]

    def column(self, col_index):
        return [row[col_index] for row in self.rows]

    def is_finished(self):
        rows = self.rows
        columns = [self.column(i) for i in range(len(rows))]
        for line in rows + columns:
            if all([isinstance(elem, bool) for elem in line]):
                return True
        return False

    def cross(self, mark):
        for y, row in enumerate(self.rows):
            for x, elem in enumerate(row):
                if elem == mark:
                    self.rows[y][x] = True
        return self.is_finished()


def load_file(filename):
    with open(filename, 'r') as f:
        groups = f.read().split('\n\n')
        order, boards = groups[0].split(','), groups[1:]
        boards = [
            Board(
                [list(map(int, row.split())) for row in board.splitlines()]
            )
            for board in boards
        ]
        return order, boards

def verify(board, char):
    pass

def part_one(boards, order):
    for mark in order:
        for board in boards:
            board.cross(mark)


if __name__ == '__main__':
    order, boards = load_file('sample.txt')
    print(part_one(boards, order))
