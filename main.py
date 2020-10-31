import argparse
from enum import Enum

from model.Sudoku import Sudoku


class AlgoType(Enum):
    BACKTRACKING = 'backtracking'
    SMT = 'smt'


def main():
    """Entry method."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', '-t',
                        type=AlgoType,
                        choices=AlgoType,
                        help='The algorithm type',
                        default=AlgoType.SMT)
    args = parser.parse_args()

    if args.type == AlgoType.BACKTRACKING:
        print('backtracking')
    else:
        from smt.smt import SmtSolver
        solution, runtime = SmtSolver.solve(Sudoku.from_string())
        print(solution)
        print("Duration: " + str(runtime) + " ms")


if __name__ == '__main__':
    main()
