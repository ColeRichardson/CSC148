from __future__ import annotations
from typing import Optional, List
from actors2 import *
import pygame
import random

LEVEL_MAPS = ["maze1.txt", "maze3.txt"]

def load_map(filename: str) -> List[List[str]]:
    """
    Load the map data from the given filename and return as a list of lists.
    """

    with open(filename) as f:
        map_data = [line.split() for line in f]
    return map_data

class Game:
    """
    This class represents the main game.
   === Attributes ===
   screen:
   player:
   keys_pressed:
   stage_width:
   size:
   goal_message:
   goal_stars:
   monster_count:

   """
   # === Private Attributes ===
   # _running:
   # _level:
   # _max_level:
   # _actors:
   #TODO complete type contracts
    """screen:
    player:
    keys_pressed:
    stage_width:
    size:
    goal_message:
    goal_stars:
    monster_count:

    _running:
    _level:
    _max_level:
    _actors:
    """
    # TODO: (Task 0) Complete the class documentation for this class by adding
    # attribute descriptions and types (make sure to separate public and
    # private attributes appropriately)

    def __init__(self) -> None:
        """
        Initialize a game that has a display screen and game actors.
        """

        self._running = False
        #changed this to 1 to test the squishy monster bouncing
        self._level = 0 # Current level that the game is in
        self._max_level = len(LEVEL_MAPS)-1
        self.screen = None
        self.player = None
        self.keys_pressed = None
        self.door = None #assign door to a variable so we can access it later

        # Attributes that get set during level setup
        self._actors = None
        self.stage_width, self.stage_height = 0, 0
        self.size = None
        self.goal_message = None

        # Attributes that are specific to certain levels
        self.goal_stars = 0  # Level 0
        self.monster_count = 0  # Level 1

        # Method that takes care of level setup
        self.setup_current_level()

    def get_level(self) -> int:
        """
        Return the current level the game is at.
        """

        return self._level

    def set_player(self, player: Player) -> None:
        """
        Set the game's player to be the given <player> object.
        """

        self.player = player

    #sets the door for the level for easy access
    def set_door(self, door: Door) -> None:
        """
        set the game's door to be the given <door> object.
        """
        self.door = door

    def add_actor(self, actor: Actor) -> None:
        """
        Add the given <actor> to the game's list of actors.
        """

        self._actors.append(actor)

    def remove_actor(self, actor: Actor) -> None:
        """
        Remove the given <actor> from the game's list of actors.
        """

        self._actors.remove(actor)

    def get_actor(self, x: int, y: int) -> Optional[Actor]:
        """
        Return the actor object that exists in the location given by
        <x> and <y>. If no actor exists in that location, return None.
        """
        # TODO: (Task 0) Move over your code from A0 here; adjust if needed
        for actor in self._actors:
            if actor.x == x and actor.y == y:
                return actor
        return None

    def door_open(self) -> bool:
        """
        returns true iff the condition for the current level has been met,
        else returns false.
        level 0: the player has collected stars equal to
        or greater than goal_stars
        level 1: the player has killed all the monsters in the level
        """
        if self.get_level() == 0:
            if self.player.get_star_count() >= self.goal_stars:
                return True
            return False
        if self.get_level() == 1:
            if self.monster_count == 0:
                return True
            return False

    def on_init(self) -> None:
        """
        Initialize the game's screen, and begin running the game.
        """

        pygame.init()
        self.screen = pygame.display.set_mode \
            (self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event: pygame.Event) -> None:
        """
        React to the given <event> as appropriate.
        """

        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            self.player.register_event(event.key)

    def game_won(self) -> bool:
        """
        Return True iff the game has been won, according to the current level.
        """

        # TODO: (Task 0) Move over your code from A0 here; adjust as needed
        if self.player.x == self.door.x and self.player.y == self.door.y:
            if self.door_open():
                return True
        return False

    def on_loop(self) -> None:
        """
        Move all actors in the game as appropriate.
        Check for win/lose conditions and stop the game if necessary.
        """

        self.keys_pressed = pygame.key.get_pressed()
        for actor in self._actors:
            actor.move(self)

        if not self.player:
            print("You lose! :( Better luck next time.")
            self._running = False

        elif self.game_won():
            if self._level == self._max_level:
                print("Congratulations, you won!")
                self._running = False
            else:
                self._level += 1
                self.setup_current_level()

        # TODO: (Task 0) Move over your code from A0 here; adjust as needed

    def on_render(self) -> None:
        """
        Render all the game's elements onto the screen.
        """

        self.screen.fill(BLACK)
        for a in self._actors:
            rect = pygame.Rect(a.x * ICON_SIZE, a.y * ICON_SIZE, ICON_SIZE, ICON_SIZE)
            self.screen.blit(a.icon, rect)

        font = pygame.font.Font('freesansbold.ttf', 12)
        text = font.render(self.goal_message, True, WHITE, BLACK)
        textRect = text.get_rect()
        textRect.center = (self.stage_width * ICON_SIZE // 2, \
                           (self.stage_height + 0.5) * ICON_SIZE)
        self.screen.blit(text, textRect)

        pygame.display.flip()

    def on_cleanup(self) -> None:
        """
        Clean up and close the game.
        """

        pygame.quit()

    def on_execute(self) -> None:
        """
        Run the game until the game ends.
        """

        self.on_init()

        while self._running:
            pygame.time.wait(100)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()

    def game_over(self) -> None:
        """
        Set the game as over (remove the player from the game).
        """

        self.player = None

    def setup_current_level(self):
        """
        Set up the current level of the game.
        """

        data = load_map(
            "../data/"+LEVEL_MAPS[self._level])  # Set the file where maze data is stored

        if self._level == 0:
            self.setup_ghost_game(data)
        elif self._level == 1:
            self.setup_squishy_monster_game(data)

    def setup_ghost_game(self, data) -> None:
        """
        Set up a game with a ghost that chases the player, and stars to collect.
        """

        w = len(data[0])
        h = len(
            data) + 1  # We add a bit of space for the text at the bottom

        self._actors = []
        self.stage_width, self.stage_height = w, h-1
        self.size = (w * ICON_SIZE, h * ICON_SIZE)

        player, chaser, door = None, None, None

        for i in range(len(data)):
            for j in range(len(data[i])):
                key = data[i][j]
                if key == 'P':
                    player = Player("../images/boy-24.png", j, i)
                elif key == 'C':
                    chaser = GhostMonster("../images/ghost-24.png", j, i)
                elif key == 'X':
                    self.add_actor(Wall("../images/wall-24.png", j, i))
                elif key == 'D':
                    door = Door("../images/door-24.png", j, i)

        self.set_player(player)
        self.add_actor(player)
        self.set_door(door) #set the door
        self.add_actor(door) # add the door to the _actors list
        player.set_smooth_move(True) # Enable smooth movement for player
        self.add_actor(chaser)
        # Set the number of stars the player must collect to win
        self.goal_stars = 5
        self.goal_message = "Objective: Collect {}".format(self.goal_stars) + \
                           " stars before the ghost gets you and head for the door"

        # Draw stars
        num_stars = 0
        while num_stars < 7:
            x = random.randrange(self.stage_width)
            y = random.randrange(self.stage_height)
            # TODO: (Task 0) Move over your code from A0 here; adjust as needed
            # Make sure the stars never appear on top of another actor
            if not isinstance(self.get_actor(x, y),(Wall, Player, GhostMonster, Star, Door)):
                self.add_actor(Star("../images/star-24.png", x, y))
                num_stars += 1

    def setup_squishy_monster_game(self, data) -> None:
        """
        Set up a game with monsters that the player must squish with boxes.
        """

        w = len(data[0])
        h = len(
            data) + 1  # We add a bit of space for the text at the bottom

        self._actors = []
        self.stage_width, self.stage_height = w, h-1
        self.size = (w * ICON_SIZE, h * ICON_SIZE)
        self.goal_message = "Objective: Squish all the monsters with the boxes " \
                           + " and head for the door"
        player, door = None, None

        for i in range(len(data)):
            for j in range(len(data[i])):
                key = data[i][j]
                if key == 'P':
                    player = Player("../images/boy-24.png", j, i)
                elif key == 'M':
                    self.add_actor(SquishyMonster("../images/monster-24.png", j, i))
                    self.monster_count += 1
                elif key == 'X':
                    self.add_actor(Wall("../images/wall-24.png", j, i))
                elif key == 'D':
                    door = Door("../images/door-24.png", j, i)

        self.set_player(player)
        self.add_actor(player)
        self.set_door(door)  # set the door
        self.add_actor(door)  # add the door to the _actors list

        # TODO: Complete this function to set up the squishy monster level
        #draw boxes
        num_boxes = 0
        while num_boxes < 12:
            x = random.randrange(self.stage_width)
            y = random.randrange(self.stage_height)
            if not isinstance(self.get_actor(x, y), (Wall, Player, SquishyMonster, Box, Door)):
                self.add_actor(Box("../images/box-24.png", x, y))
                num_boxes += 1



