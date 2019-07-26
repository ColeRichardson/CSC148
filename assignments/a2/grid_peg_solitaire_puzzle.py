"""
Assignment 2: Automatic Puzzle Solver
==============================
This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

=== Module Description ===
This module contains the class required to solve grid peg solitaire puzzles.
"""
from __future__ import annotations
from typing import List, Set
from puzzle import Puzzle

class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker: List[List[str]], marker_set: Set[str]):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        Note: The symbol "#" is for unused, "*" is for peg, "." is for empty

        Precondition:
        - marker is a non-empty list of lists representing an m x n grid
        - the strings in marker are all a valid string from marker_set
        """
        # Private Attributes
        # _marker
        #   the m x n solitaire grid with some pegs, spaces and unused spots
        # _marker_set
        #   the possible symbols on the grid, representing different spots

        _marker: str
        _marker_set: str

        self._marker, self._marker_set = marker, marker_set

    # TODO (Task 2)
    # implement __eq__ and __str__
    # __repr__ is optional / up to you
    def __str__(self):
        """returns a human readable string representation
         of this GridPegSolitairePuzzle"""
        s = ''
        for row in self._marker:
            for item in row:
                s += item
            s += '\n'
        return s

    def __eq__(self, other: Union[GridPegSolitairePuzzle, Any]) -> bool:
        """
        Return whether this GridPegSolitairePuzzle is equivalent to the <other>.
        """
        return type(other) == type(self) and self._marker == other._marker and \
               self._marker_set == other._marker_set


    # TODO (Task 3)
    # override extensions
    # legal extensions consist of all configurations that can be reached by
    # making a single jump from this configuration

    # TODO (Task 3)
    # override is_solved
    # A configuration is solved when there is exactly one "*" left
    def is_solved(self):  #TODO Docstrings/type contracts
        """return whether this GridPegSolitairePuzzle is solved.
        >>> grid = [["*", "*", "*", "*", "*"], \
                    ["*", "*", "*", "*", "*"], \
                    ["*", "*", "*", "*", "*"], \
                    ["*", "*", ".", "*", "*"], \
                    ["*", "*", "*", "*", "*"]]
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> gpsp.is_solved()
        False
        >>> grid = [[".", ".", ".", ".", "."], \
                    [".", ".", ".", ".", "."],\
                    [".", ".", ".", ".", "."],\
                    [".", ".", ".", ".", "."],\
                    [".", ".", ".", ".", "*"]]
        >>> gpsp1 = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> gpsp1.is_solved()
        True

        """
        temp_list = []
        for row in self._marker:
            temp_list.extend(row)
        return temp_list.count("*") == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))
