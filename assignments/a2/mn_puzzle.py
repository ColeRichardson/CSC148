"""
Assignment 2: Automatic Puzzle Solver
==============================
This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

=== Module Description ===
This module contains the class required to solve mn puzzles.
"""

from __future__ import annotations
from typing import Tuple
from puzzle import Puzzle

class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """
    # Private Attributes
    # _n
    #   the height of the grid
    # _m
    #   the width of the grid
    # _from_grid
    #   the initial grid arrangement this puzzle begins at
    # _to_grid
    #   the goal grid arrangement this puzzle aims to reach
    _n: int
    _m: int
    _from_grid: Tuple
    _to_grid: Tuple

    def __init__(self, from_grid: Tuple, to_grid: Tuple) -> None:
        """
        MNPuzzle in state from_grid, working towards
        state to_grid.

        Note:
            Grid symbols are represented as letters or numerals
            The empty space is represented as a "*"

        Preconditions:
        - both from_grid and to_grid are rectangular m x n grids
        """

        self._n, self._m = len(from_grid), len(from_grid[0])
        self._from_grid, self._to_grid = from_grid, to_grid

    # TODO (Task 6)
    # implement __eq__ and __str__
    # __repr__ is optional / up to you

    # TODO (Task 7)
    # override extensions
    # legal extensions are configurations that can be reached by swapping one
    # symbol to the left, right, above, or below "*" with "*"

    # TODO (Task 7)
    # override is_solved
    # a configuration is solved when from_grid is the same as to_grid
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    # Comment out the code below as you solve necessary parts of the assignment
    """
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    """
