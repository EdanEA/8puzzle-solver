# 8puzzle-solver
Python-based 8-puzzle solver, using best-first search. Was created as a way of implementing some of the information detailed in the first few chapters of [Artificial Intelligence: A Modern Approach](https://aima.cs.berkeley.edu/). 

## Usage
`git clone` files to your computer
Run `python3 main.py`

## How it works
The script randomly generates and order and attempts to find a solution, if deemed solvable using inversions. This order is put into a grid where moves can be determined and such. The states are then put into a node and continually builds a tree of states, determing which is best using a heuristic function to determine how to proceed continually. Once a goal state is reached, the solution is put into a database and a new order is generated.
