from __future__ import annotations  # Reference: Reading on Type Annotations
from typing import Tuple, List, Optional
from stack import Stack

import random


class MazeGame:
    """
    A game where a player moves through a grid to reach some treasure.

    === Attributes ===
    width: The width of the maze
    height: The height of the maze
    player: The player object in the game
    """
    # === Private Attributes ===
    # _gold_coord: The coordinates in the maze where the gold is
    # _grid: The grid representing the whole maze
    width: int
    height: int
    player: Player
    _gold_coord: int
    _grid: List[List[str]]
    move_stack = Stack()
    #move_stack.push((0,0))

    def __init__(self, width: int, height: int, player: Player) -> None:
        '''
        Construct a new MazeGame with the given <width> and <height>,
        and a <player>. MazeGame should also place a "gold" at
        a randomly chosen coordinate on the far edge of the grid.
        '''

        self.width = width
        self.height = height
        self.player = player

        # place the gold at a random spot on the far edge of the grid
        self._gold_coord = (width - 1, random.randint(1, height - 1))

        self._grid = []
        self.make_grid()

    def make_grid(self) -> None:
        '''
        Given width, height and positions of player and gold,
        append things to this maze's grid.
        '''

        for i in range(self.height):
            self._grid.append([])
            for j in range(self.width):
                self._grid[i].append('(_)')

        self._grid[self.player.y][self.player.x] = '(x)'
        self._grid[self._gold_coord[1]][self._gold_coord[0]] = '(*)'

    def play_game(self) -> None:
        '''
        Play the game, with each player taking turns making a move, until
        one player reaches the gold.
        Players each keep track of their wins and losses.
        '''

        # print out the starting state of the maze
        print(self)
        print('------------')

        # if no one has reached the gold yet,
        # play one turn of the game (one player makes one move)
        while not (self.player.x, self.player.y) == (self._gold_coord[0], \
                                                     self._gold_coord[1]):
            self.play_one_turn()

        print('Yay, you won, {}!'.format(self.player.name))

    def get_new_position(self, d: str) -> Optional[Tuple[int, int]]:
        '''
        Given a direction represented as a string "N", "S", "E", or "W"
        (for moving North, South, East or West respectively), return the new
        position. If the new position is not valid (i.e. falls outside of
        the grid), return None.
        '''

        direction_dict = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}
        dx, dy = direction_dict[d]
        new_x = self.player.x + dx
        new_y = self.player.y + dy

        if (0 <= new_x < self.width) and (0 <= new_y < self.height):
            return new_x, new_y
        else:
            return None

    def update_grid(self, new_position: Tuple[int, int]) -> None:
        '''
        Move player to the given new position in grid.
        '''

        # keep track of the Player's current position before they move
        old_x, old_y = self.player.x, self.player.y
        self.player.move(new_position)
        # update grid to reflect updated coordinates for current_player
        self._grid[self.player.y][self.player.x] = self._grid[old_y][old_x]
        self._grid[old_y][old_x] = '(_)'

    def play_one_turn(self) -> None:
        '''
        Play one turn of the game. Turn could involve moving one place,
        attempting to move one place, or undoing the most recent move.
        '''

        # get the direction the Player wants to move
        direction = self.player.get_direction()

        if (direction == 'U'):
            self.undo_last_move()
        else:
            # new_position gets set to None if move is not valid
            new_position = self.get_new_position(direction)

            if new_position:  # Note: this is same as "if new_position != None"
                self.move_stack.push((self.player.x, self.player.y))
                self.update_grid(new_position)
                print("Player {} moved {}.".format(self.player.name, direction))
            else:
                print("Player {} attempted to move {}. Way is blocked." \
                      .format(self.player.name, direction))

        # print current state of game
        print(self)
        print('------------')

    def undo_last_move(self) -> None:
        '''
        Update the grid to the state it was in before previous move was made.
        If no moves were previously made, print out the message "Can't undo".
        '''

        # TODO: IMPLEMENT THIS AS DESCRIBED IN LAB INSTRUCTIONS
        if self.move_stack.is_empty():
            print("can't undo")
        else:
            #move the player back to previous move
            self.update_grid(self.move_stack.pop())
        pass

    def __str__(self) -> str:
        '''
        Return string representation of the game's grid.
        '''

        s = ''
        for row in self._grid:
            s += ''.join(row) + "\n"
        return s.strip()


# TODO: IMPLEMENT PLAYER CLASS AS DESCRIBED IN LAB INSTRUCTIONS
#       REMEMBER TO INCLUDE PROPER DOCSTRINGS AND TYPE CONTRACTS
class Player:
    """stores the attributes and methods for a player of the game.
    """
    def __init__(self, name, x, y):
        """initializes the player
        :param name:
        :param x:
        :param y:
        """
        self.name = name
        self.x = x
        self.y = y

    def move(self, new_position):
        """ updates the players x and y to represent the co-ordinates they have moved to

        :return:
        """
        self.x = new_position[0]
        self.y = new_position[1]

    def get_direction(self) -> str:
        """
        prompts the player for the direction they would like to move to,
        returns this value.
        :return:
        """
        direction = "a"
        directions = "NSEWU"
        while direction not in directions:
            direction = input('what direction do you want to move in? (N, S, E, W, U)')
        return direction

def main() -> None:
    """Prompt the user to configure and play the game."""

    width = int(input("Width: "))
    height = int(input("Height: "))

    name = input("What is your name? ")
    p1 = Player(name, 0, 0)  # make a player at position (0,0)

    play_again = True
    while play_again:
        g = MazeGame(width, height, p1)
        g.play_game()
        # reset player locations at end of round
        p1.move((0, 0))
        play_again = input('Again? (y/n) ') == 'y'


if __name__ == '__main__':
    main()
