import string

import numpy as np


class Sudoku:
    def __init__(self, data: np.ndarray = None):
        if data is not None and data.size == 9 * 9:
            self.data = data
        else:
            self.data = None

    def __str__(self):
        """ Returns a pretty representation of the grid as string. """

        if self.data is None:
            return ""
        lines = []

        for row in range(9):
            if row % 3 == 0:
                lines.append("+–––––––––+–––––––––+–––––––––+")

            line = ''

            for col in range(9):
                line += "{1} {0} ".format(self.data[row][col], '|' if col % 3 == 0 else '')

            lines.append(line + '|')

        lines.append("+–––––––––+–––––––––+–––––––––+")
        return '\n'.join(lines)

    def get_ndindex(self) -> np.ndindex:
        return np.ndindex(self.data.shape)

    def get_item(self, i, j):
        return self.data[i, j]

    def is_set(self, i, j):
        return self.get_item(i, j) != '.'

    def to_list(self):
        return self.data.tolist()

    @staticmethod
    def from_string(puzzle: string):
        data = [ch for ch in puzzle]
        return Sudoku(np.resize(data, (9, 9)))
