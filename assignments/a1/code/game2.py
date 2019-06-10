from __future__ import annotations
from typing import Optional, List
from actors2 import *
import pygame
import random

LEVEL_MAPS = ["maze1.txt", "maze3.txt", "final_maze.txt"]


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
   screen: the window where the game is being played
   player: player object, holds information about the player
   keys_pressed: holds the keys that are being pressed by the user
   stage_width: holds the width of the stage
   stage_height: holds the height of the stage
   size: the size of the pygame screen
   goal_message: message that is displayed to user at the bottom of the screen
   goal_stars: the number of stars the player must collect to win
   monster_count: the number of monsters in the stage
   door: the door object for the current level
   boss: the BossMonster object for level 2
   num_bombs: number of bombs in level 2
   start_time: the time when level 2 is loaded
   end_time: the time when the BossMonster is found in on_loop, used to spawn
   bombs and chasers for level 2
   num_chasers: the number of chasers in level 2
   """

    # === Private Attributes ===
    # _running:
    # the state of the game, either True or False
    # _level:
    # the level that the game is currently in
    # _max_level:
    # the maximum level that the game can be played in
    # _actors:
    # a list of actors objects

    screen: pygame.display
    player: player
    keys_pressed: pygame.key
    stage_width: int
    stage_height: int
    size: int
    goal_message: str
    goal_stars: int
    monster_count: int
    door: door
    boss: boss
    num_bombs: int
    start_time: int
    end_time: int
    num_chasers: int

    _running: bool
    _level: int
    _max_level: int
    _actors: list

    def __init__(self) -> None:
        """
        Initialize a game that has a display screen and game actors.
        """

        self._running = False
        self._level = 2  # Current level that the game is in
        self._max_level = len(LEVEL_MAPS)-1
        self.screen = None
        self.player = None
        self.keys_pressed = None
        self.door = None  # assign door to a variable so we can access it later
        self.boss = None

        # Attributes that get set during level setup
        self._actors = None
        self.stage_width, self.stage_height = 0, 0
        self.size = None
        self.goal_message = None

        # Attributes that are specific to certain levels
        self.goal_stars = 0  # Level 0
        self.monster_count = 0  # Level 1

        # Attributes that are specific to level 2
        self.num_bombs = 0
        self.start_time = 0
        self.end_time = 0
        self.num_chasers = 0

        # Method that takes care of level setup
        self.setup_current_level()

    def get_level(self) -> int:
        """
        Return the current level the game is at.
        """

        return self._level

    def get_num_bombs(self) -> int:
        """
        return the number of bombs in the current stage.
        """
        return self.num_bombs

    def get_num_chasers(self) -> int:
        """
        return the number of chasers in the current stage.
        """
        return self.num_chasers

    def set_player(self, player: Player) -> None:
        """
        Set the game's player to be the given <player> object.
        """

        self.player = player

    # sets the door for the level for easy access
    def set_door(self, door: Door) -> None:
        """
        set the game's door to be the given <door> object.
        """
        self.door = door

    def set_boss(self, boss: BossMonster):
        """
        set the game's boss to be the given <BossMonster> object.
        """
        self.boss = boss

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
        if self.get_level() == 2:
            if self.num_chasers == 0 and self.player.has_key and not self.boss:
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
        # checks if player is at the door location
        if self.player.x == self.door.x and self.player.y == self.door.y:
            # checks if win condition has been met for current level
            if self.door_open():
                return True
        return False

    def on_loop(self) -> None:
        """
        Move all actors in the game as appropriate.
        and for level 2, check time and spawn bombs and chasers if BossMonster
        exists in self._actors.
        Check for win/lose conditions and stop the game if necessary.
        """

        self.keys_pressed = pygame.key.get_pressed()
        for actor in self._actors:
            actor.move(self)
            if isinstance(actor, BossMonster):
                self.end_time = pygame.time.get_ticks()
                if self.end_time - self.start_time >= 5000:
                    self.start_time = pygame.time.get_ticks()
                    actor.spawn_bombs(self)
                    actor.spawn_chaser(self)

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
        # Set the file where maze data is stored
        data = load_map(
            "../data/"+LEVEL_MAPS[self._level])

        if self._level == 0:
            self.setup_ghost_game(data)
        elif self._level == 1:
            self.setup_squishy_monster_game(data)
        elif self._level == 2:
            self.setup_boss_game(data)

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
        self.set_door(door)  # set the door
        self.add_actor(door)  # add the door to the _actors list
        player.set_smooth_move(True)  # Enable smooth movement for player
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
            # Make sure the stars never appear on top of another actor
            if not isinstance(self.get_actor(x, y), Actor):
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

        # draw boxes, also check if there is an actor there
        num_boxes = 0
        while num_boxes < 12:
            x = random.randrange(self.stage_width)
            y = random.randrange(self.stage_height)
            if not isinstance(self.get_actor(x, y), Actor):
                self.add_actor(Box("../images/box-24.png", x, y))
                num_boxes += 1

    def setup_boss_game(self, data) -> None:
        """
        set up a game where the player must avoid the chasers and bombs
        spawned by the boss and kill the boss by picking up power ups.
        then pick up the key to open the door.
        """
        w = len(data[0])
        h = len(data) + 1

        self._actors = []
        self.stage_width, self.stage_height = w, h - 1
        self.size = (w * ICON_SIZE, h * ICON_SIZE)
        self.goal_message = "Objective: defeat the boss by picking up the key "\
            + "read console for further instructions"
        print("Welcome to the boss level, avoid the boss, chasers and bombs,"
              + " if they touch you they will kill you, if you have a shield \n"
              + "you will kill them instead, except for the boss, to kill "
              + "him you will need the key, once you've killed the boss and all\n"
              + "his chasers, make sure you have the key and head for the door.")

        player, boss, door = None, None, None

        for i in range(len(data)):
            for j in range(len(data[i])):
                key = data[i][j]
                if key == 'P':
                    player = Player("../images/boy-24.png", j, i)
                elif key == 'B':
                    boss = BossMonster("../images/boss-24.png", j, i)
                elif key == 'X':
                    self.add_actor(Wall("../images/wall-24.png", j, i))
                elif key == 'D':
                    door = Door("../images/door-24.png", j, i)
                elif key == 'K':
                    self.add_actor(Key("../images/key-24.png", j, i))
                elif key == 'H':
                    self.add_actor(Shield("../images/shieldup-24.png", j, i))

        self.set_player(player)
        self.add_actor(player)
        player.set_smooth_move(True)
        self.set_door(door)  # set the door
        self.add_actor(door)  # add the door to the _actors list
        self.set_boss(boss)
        self.add_actor(boss)
        # start timer for spawning chasers/bombs
        self.start_time = pygame.time.get_ticks()
