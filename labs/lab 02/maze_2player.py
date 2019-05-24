from __future__ import annotations  # Reference: Reading on Type Annotations
from typing import Tuple, List, Optional

import random
from stack import Stack


class MazeGame:
    """
    A game where two players move through a grid in a race to
    be the first to reach some treasure.

    === Attributes ===
    width: The width of the maze
    height: The height of the maze
    player1: The first player object in the game
    player2: The second player object in the game
    """
    # === Private Attributes ===
    # _gold_coord: The coordinates in the maze where the gold is
    # _grid: The grid representing the whole maze
    width: int
    height: int
    player: Player
    _gold_coord: int
    _grid: List[List[str]]

    def __init__(self, width: int, height: int, \
                 player1: Player, player2: Player) -> None:
        '''
        Construct a new MazeGame with the given <width> and <height>,
        and two players. MazeGame should also place a "gold" at
        a randomly chosen coordinate on the far edge of the grid.
        '''

        self.width = width
        self.height = height
        self.players = (player1, player2)
        # place the gold at a random spot on the far edge of the grid
        self._gold_coord = (width - 1, random.randint(1, height - 1))

        self._grid = []
        self.make_grid()

        self.turn = 0  # keep track of whose turn it is out of the two players

    def make_grid(self) -> None:
        '''
        Given width, height and positions of player and gold,
        append things to this maze's grid.
        '''

        for i in range(self.height):
            self._grid.append([])
            for j in range(self.width):
                self._grid[i].append('(_)')

        self._grid[self.players[0].y][self.players[0].x] = '(x)'
        self._grid[self.players[1].y][self.players[1].x] = '(o)'
        self._grid[self._gold_coord[1]][self._gold_coord[0]] = '(*)'

    def whose_turn(self, count: int) -> Player:
        '''
        Return the Player whose turn it is.
        '''

        if count % 2 == 0:
            next_player = self.players[0]
        else:
            next_player = self.players[1]
        return next_player

    def play_game(self) -> None:
        '''
        Play the game, with each player taking turns making a move, until
        one player reaches the gold.
        Players each keep track of their wins and losses.
        '''

        # print out the starting state of the maze
        print(self)
        print('------------')

        winner = None
        while (not winner):
            if (self.players[0].x, self.players[0].y) == \
                    (self._gold_coord[0], self._gold_coord[1]):
                winner = self.players[0]
            elif (self.players[1].x, self.players[1].y) == \
                    (self._gold_coord[0], self._gold_coord[1]):
                winner = self.players[1]
            else:
                # if no one has reached the gold yet,
                # play one turn of the game (one player makes one move)
                self.play_one_turn()

        print('And {} is the winner!!!'.format(winner.name))

    def get_new_position(self, current_player: Player, other_player: Player, \
                         d: str) -> Optional[Tuple[int, int]]:
        '''
        Given the current player, the other player, and a direction represented
        as a string "N", "S", "E", or "W" (for moving North, South, East or West
        respectively), return the new position. If the new position is not valid
        (falls outside of the grid, or is already occupied by the other player),
        return None.
        '''

        direction_dict = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}
        dx, dy = direction_dict[d]
        new_x = current_player.x + dx
        new_y = current_player.y + dy

        if (0 <= new_x < self.width) and (0 <= new_y < self.height) and \
                not (new_x, new_y) == (other_player.x, other_player.y):
            return new_x, new_y
        else:
            return None

    def update_grid(self, player: Player,
                    new_position: Tuple[int, int]) -> None:
        '''
        Given a player and new position, move that player to new position in grid.
        '''

        # keep track of the Player's current position before they move
        old_x, old_y = player.x, player.y
        player.move(new_position)
        # update grid to reflect updated coordinates for current_player
        self._grid[player.y][player.x] = self._grid[old_y][old_x]
        self._grid[old_y][old_x] = '(_)'

    def play_one_turn(self) -> None:
        '''
        Play one turn of the game. Turn could involve moving one place,
        attempting to move one place, or undoing the most recent move.
        '''

        # get the Player whose turn it currently is
        current_player = self.whose_turn(self.turn)

        # get the other Player in the game
        other_player = self.whose_turn(self.turn - 1)

        # get the direction the Player wants to move
        direction = current_player.get_direction()

        # this sets new_position to None if move is not valid
        new_position = self.get_new_position(current_player, \
                                             other_player, direction)

        if new_position:  # Note: this is the same as "if new_position != None"
            self.update_grid(current_player, new_position)
            print("Player {} moved {}.".format(current_player.name, direction))
        else:
            print("Player {} attempted to move {}. Way is blocked." \
                  .format(current_player.name, direction))

        # print current state of game
        print(self)
        print('------------')

        self.turn += 1

    def __str__(self) -> str:
        '''
        Return string representation of the game's grid.
        '''

        s = ''
        for row in self._grid:
            s += ''.join(row) + "\n"
        return s.strip()


# TODO: IMPLEMENT PLAYER CLASSES AS DESCRIBED IN PART 3 OF LAB
#       REMEMBER TO INCLUDE PROPER DOCSTRINGS AND TYPE CONTRACTS
class Player:
    pass


def make_player(player_name: str, player_type: str, x: int, y: int) -> Player:
    """
    Given a player name, player type (either c for computer or u for user),
    and an x and y coordinate, create a new Player of the
    right type and return it.
    """

    if player_type == "c":
        return ComputerPlayer(player_name, x, y)
    elif player_type == "u":
        return UserPlayer(player_name, x, y)


def main():
    """Prompt the user to configure and play the game."""

    width = int(input("Width: "))
    height = int(input("Height: "))

    name = input("What is p1's name? ")
    # make the first player a User at position (0,0)
    p1 = make_player(name, 'u', 0, 0)

    player_type = input("Is p2 a user or a computer? " + \
                        "Enter 'u' for user, 'c' for computer. ")
    name = input("What is p2's name? ")
    # make the second player either a User or Computer based
    # on response to prompt, at position (0, 1)
    p2 = make_player(name, player_type.lower(), 0, 1)

    play_again = True
    while play_again:
        g = MazeGame(width, height, p1, p2)
        g.play_game()
        # reset player locations at end of round
        p1.move((0, 0))
        p2.move((0, 1))
        play_again = input('Again? (y/n) ') == 'y'


if __name__ == '__main__':
    main()
