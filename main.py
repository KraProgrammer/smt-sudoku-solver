import argparse
from enum import Enum

from model.Sudoku import Sudoku


class AlgoType(Enum):
    BACKTRACKING = 'backtracking'
    SMT = 'smt'


SAMPLE_INPUT_1 = '..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97..'
SAMPLE_INPUT_2 = '1.......2.9.4...5...6...7...5.9.3.......7.......85..4.7.....6...3...9.8...2.....1'


def main():
    """Entry method."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', '-t',
                        type=AlgoType,
                        choices=AlgoType,
                        help='The algorithm type',
                        default=AlgoType.SMT)
    parser.add_argument('--input', '-i',
                        help='The sudoku',
                        default=SAMPLE_INPUT_1)
    args = parser.parse_args()

    if args.type == AlgoType.BACKTRACKING:
        print('backtracking')
    else:
        from smt.smt import SmtSolver
        solution, runtime = SmtSolver.solve(Sudoku.from_string(args.input))
        print(solution)
        print("Duration: " + str(runtime) + " ms")


if __name__ == '__main__':
    main()
