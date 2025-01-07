# 8puzzle-solver
Python-based 8-puzzle solver, using best-first search. Was created as a way of implementing some of the information detailed in the first few chapters of [Artificial Intelligence: A Modern Approach](https://aima.cs.berkeley.edu/). 

## Usage
`git clone` files to your computer

Run `python3 main.py`

## How it works
The script randomly generates an order for a puzzle and attempts to find a solution, if deemed solvable using inversions. The state of the puzzle is represented as a string where a grid is read left-to-right and top-to-bottom:

```
1 | 2 | 3
4 | 5 | 6
7 | 8 | 0
```

would be "123456780" where 0 is the empty space and a number n is the nth tile for the ordered sequence. This order is put into an array where possible moves can be determined and made. Best-first search works from the initial state and performs possible moves as informed by a heuristic function. Different states are stored in nodes, which create a tree structure, with the initial state being the root. Moves are made continually until a goal state is reached and the goal state is returned, from which the path from root to goal can be backtracked. The solution is stored into a database and then randomly generates another iniital state and the steps repeat.
