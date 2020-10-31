import time

import numpy as np
from z3 import Solver, Int, Distinct, sat

from model.Sudoku import Sudoku


class SmtSolver:

    @staticmethod
    def solve(sudoku: Sudoku):
        """
        Method solving the given sudoku puzzle using Z3 solver.

        :param sudoku: The unsolved sudoku object.
        :return: The solved sudoku and the runtime.
        """
        print(sudoku)

        solver = Solver()
        symbols = [[Int('cell%d%d' % (r, c)) for c in range(9)] for r in range(9)]

        for row, col in sudoku.get_ndindex():
            if sudoku.is_set(row, col):
                solver.add(symbols[row][col] == int(sudoku.get_item(row, col)))

        SmtSolver._create_sudoku_constraints(solver, symbols)

        start = time.perf_counter()
        check = solver.check()
        end = time.perf_counter()
        runtime = (end - start) * 1000

        if check == sat:
            model = solver.model()

            matrix = []
            for r in range(9):
                row = []
                for c in range(9):
                    row.append(str(model[symbols[r][c]]))
                matrix.append(row)
            return Sudoku(np.array(matrix)), runtime
        else:
            return Sudoku, 0

    @staticmethod
    def _create_sudoku_constraints(solver, symbols):
        for r in range(9):
            for c in range(9):
                solver.add(symbols[r][c] >= 1)
                solver.add(symbols[r][c] <= 9)
        for r in range(9):
            solver.add(Distinct(symbols[r][0],
                                symbols[r][1],
                                symbols[r][2],
                                symbols[r][3],
                                symbols[r][4],
                                symbols[r][5],
                                symbols[r][6],
                                symbols[r][7],
                                symbols[r][8]))
        for c in range(9):
            solver.add(Distinct(symbols[0][c],
                                symbols[1][c],
                                symbols[2][c],
                                symbols[3][c],
                                symbols[4][c],
                                symbols[5][c],
                                symbols[6][c],
                                symbols[7][c],
                                symbols[8][c]))
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                solver.add(Distinct(symbols[r + 0][c + 0],
                                    symbols[r + 0][c + 1],
                                    symbols[r + 0][c + 2],
                                    symbols[r + 1][c + 0],
                                    symbols[r + 1][c + 1],
                                    symbols[r + 1][c + 2],
                                    symbols[r + 2][c + 0],
                                    symbols[r + 2][c + 1],
                                    symbols[r + 2][c + 2]))
