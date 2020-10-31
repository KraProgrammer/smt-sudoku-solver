import time

import numpy as np

from model.Sudoku import Sudoku


class BtSolver:
    """
    https://www.geeksforgeeks.org/sudoku-backtracking-7/
    """

    @staticmethod
    def find_empty_location(arr, l):
        """
        Function to Find the entry in the Grid that is still not used Searches the grid to find an entry
        that is still unassigned.
        :param l:
        :return:
        """
        for row in range(9):
            for col in range(9):
                if arr[row][col] == '.':
                    l[0] = row
                    l[1] = col
                    return True
        return False

    @staticmethod
    def used_in_row(arr, row, num):
        """
         Returns a boolean which indicates whether any assigned entry in the specified row matches the given number.
        """
        for i in range(9):
            if arr[row][i] == num:
                return True
        return False

    @staticmethod
    def used_in_col(arr, col, num):
        """
        Returns a boolean which indicates whether any assigned entry in the specified column matches the given number.
        """
        for i in range(9):
            if arr[i][col] == num:
                return True
        return False

    @staticmethod
    def used_in_box(arr, row, col, num):
        """
        Returns a boolean which indicates whether any assigned entry within the specified 3x3 box matches the given number
        """
        for i in range(3):
            for j in range(3):
                if arr[i + row][j + col] == num:
                    return True
        return False

    @staticmethod
    def check_location_is_safe(arr, row, col, num):
        """
        Checks whether it will be legal to assign num to the given row, col. Returns a boolean which indicates
        whether it will be legal to assign num to the given row, col location.
        """
        return not BtSolver.used_in_row(arr, row, num) \
               and not BtSolver.used_in_col(arr, col, num) \
               and not BtSolver.used_in_box(arr, row - row % 3, col - col % 3, num)

    @staticmethod
    def bt_solve(arr: []):
        rc_list = [0, 0]

        if not BtSolver.find_empty_location(arr, rc_list):
            return arr, True

        row = rc_list[0]
        col = rc_list[1]

        for num in range(1, 10):
            if BtSolver.check_location_is_safe(arr, row, col, str(num)):
                arr[row][col] = str(num)

                arr, result = BtSolver.bt_solve(arr)
                if result:
                    return arr, result

            arr[row][col] = '.'

        return arr, False

    @staticmethod
    def solve(sudoku: Sudoku):
        """
        Method solving the given sudoku puzzle using a backtracking algorithm solver.

        :param sudoku: The unsolved sudoku object.
        :return: The solved sudoku and the runtime.
        """
        print(sudoku)

        start = time.perf_counter()
        arr, result = BtSolver.bt_solve(sudoku.to_list())
        end = time.perf_counter()
        runtime = (end - start) * 1000

        if result:
            return Sudoku(np.array(arr)), runtime
        else:
            return Sudoku(), 0
