import argparse

from enum import Enum


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
        print('smt')


if __name__ == '__main__':
    main()
