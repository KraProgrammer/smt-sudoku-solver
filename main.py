import argparse
from enum import Enum

from backtracking.bt import BtSolver
from model.Sudoku import Sudoku
from smt.smt import SmtSolver


class AlgoType(Enum):
    BACKTRACKING = 'backtracking'
    SMT = 'smt'
    ALL = 'all'


SAMPLE_INPUT_E = '3.65.84..52........87....31..3.1..8.9..863..5.5..9.6..13....25........74..52.63..'
SAMPLE_INPUT_M = '..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97..'
SAMPLE_INPUT_H = '1.......2.9.4...5...6...7...5.9.3.......7.......85..4.7.....6...3...9.8...2.....1'


def main():
    """Entry method."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', '-t',
                        type=AlgoType,
                        choices=AlgoType,
                        help='The algorithm type',
                        default=AlgoType.ALL)
    parser.add_argument('--input', '-i',
                        help='The sudoku',
                        default=SAMPLE_INPUT_H)
    args = parser.parse_args()

    if args.type == AlgoType.BACKTRACKING:
        solution, runtime = BtSolver.solve(Sudoku.from_string(args.input))
        _print_result(runtime, solution)
    elif args.type == AlgoType.SMT:

        solution, runtime = SmtSolver.solve(Sudoku.from_string(args.input))
        _print_result(runtime, solution)
    else:
        print("BT:")
        solution, runtime = BtSolver.solve(Sudoku.from_string(args.input))
        _print_result(runtime, solution)
        print("SMT:")
        solution, runtime = SmtSolver.solve(Sudoku.from_string(args.input))
        _print_result(runtime, solution)


def _print_result(runtime, solution):
    print(solution)
    print("Duration: " + str(runtime) + " ms")


if __name__ == '__main__':
    main()
