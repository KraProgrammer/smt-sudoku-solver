# SMT-solver-based Sudoku solver 

A Sudoku is a number puzzle in which the numbers 1 to 9 must be placed into a grid of cells
so that each row or column contains only one of each number. 
Some of the cells are filled initially.

This repo contains the logic to solve sudoku puzzles using a basic backtracking algorithm
and an smt-solver-based approach. 

### Backtracking
Backtracking is a general algorithm for finding all (or some) solutions to some computational 
problems, notably constraint satisfaction problems 
that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") 
as soon as it determines that the candidate cannot possibly be completed to a valid solution.

### Satisfiability modulo theories (SMT) solver
The satisfiability modulo theories (SMT) problem is a decision problem for logical formulas
with respect to combinations of background theories expressed in classical first-order logic with equality.
SMT solvers are applications that calculate the satisfiability of logical formulas in the SMT domain. 

## Requirements 

- Python 3.7
- requirements.txt

## Setup Python environment with CLI

```powershell
python -m venv <venv_name>
.\<venv_name>\Scripts\activate
python -m pip install -r requirements.txt
```

## Comparing backtracking with SMT solving

Fundamental performance measurement resulted in:

### Easy sudoku

- BT:  Duration: ~11 ms
- SMT: Duration: ~40 ms

### Moderate sudoku

- BT:  Duration: ~150 ms
- SMT: Duration: ~230 ms

### Hard sudoku

- BT:  Duration: ~4000 ms
- SMT: Duration: ~300 ms
