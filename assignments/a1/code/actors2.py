from __future__ import annotations
import pygame
from typing import Optional
from settings import *
import random


class Actor:
    """
    A class to represent all the game's actors. This class includes any
    attributes/methods that every actor in the game must have.

    This is an abstract class. Only subclasses should be instantiated.

    === Public Attributes ===
    x:
        x coordinate of this actor's location on the stage
    y:
        y coordinate of this actor's location on the stage
    icon:
        the image representing this actor
    """
    x: int
    y: int
    icon: pygame.Surface

    def __init__(self, icon_file, x, y):
        """Initialize an actor with the given image <icon_file> and the
        given <x> and <y> position on the game's stage.
        """

        self.x, self.y = x, y
        self.icon = pygame.image.load(icon_file)

    def move(self, game: 'Game') -> None:
        """Move this actor by taking one step of its animation."""

        raise NotImplementedError


class Player(Actor):
    """
    A class to represent a Player in the game.
    === Attributes ===
    Shields: the number of shields the player has
    has_key: True if the player has collected the key, False otherwise.
    """
    # === Private Attributes ===
    # _stars_collected:
    #       the number of stars the player has collected so far
    # _last_event:
    #       keep track of the last key the user pushed down
    # _smooth_move:
    #       represent on/off status for smooth player movement

    x: int
    y: int
    icon: pygame.Surface
    shields: int
    has_key: bool
    _stars_collected: int
    _last_event: Optional[int]
    _smooth_move: bool

    def __init__(self, icon_file: str, x: int, y: int) -> None:
        """Initialize a Player with the given image <icon_file> at the position
        <x> and <y> on the stage."""

        super().__init__(icon_file, x, y)
        self._stars_collected = 0
        self._last_event = None # This is used for precise movement
        self._smooth_move = False # Turn this on for smooth movement
        self.shields = 0
        self.has_key = False # the player does not start with the key

    def set_smooth_move(self, status: bool) -> None:
        """
        Set the <status> of whether or not the player will move smoothly.
        """

        self._smooth_move = status

    def get_star_count(self) -> int:
        """
        Return the number of stars collected.
        """

        return self._stars_collected

    def register_event(self, event: int) -> None:
        """
        Keep track of the last key <event> the user made.
        """

        self._last_event = event

    def move(self, game: 'Game') -> None:
        """
        Move the player on the <game>'s stage based on keypresses.
        """

        evt = self._last_event

        if self._last_event:
            dx, dy = 0, 0

            # Smooth movement used by the ghost level
            if self._smooth_move:
                if game.keys_pressed[pygame.K_LEFT] or game.keys_pressed[pygame.K_a]:
                    dx -= 1
                if game.keys_pressed[pygame.K_RIGHT] or game.keys_pressed[pygame.K_d]:
                    dx += 1
                if game.keys_pressed[pygame.K_UP] or game.keys_pressed[pygame.K_w]:
                    dy -= 1
                if game.keys_pressed[pygame.K_DOWN] or game.keys_pressed[pygame.K_s]:
                    dy += 1

            # Precise movement used by the squishy monster level
            elif not self._smooth_move:
                if evt == pygame.K_LEFT or evt == pygame.K_a:
                    dx -= 1
                if evt == pygame.K_RIGHT or evt == pygame.K_d:
                    dx += 1
                if evt == pygame.K_UP or evt == pygame.K_w:
                    dy -= 1
                if evt == pygame.K_DOWN or evt == pygame.K_s:
                    dy += 1
                self._last_event = None

            new_x, new_y = self.x + dx, self.y + dy

            # Check if move is possible
            if isinstance(game.get_actor(new_x, new_y), Wall):
                new_x = self.x
                new_y = self.y
            # check if player is trying to pickup shield
            elif isinstance(game.get_actor(new_x, new_y), Shield):
                game.get_actor(new_x, new_y).apply_power_up(game)
                game.remove_actor(game.get_actor(new_x, new_y))
                self.x = new_x
                self.y = new_y
            # check if the player is trying to pickup a key
            elif isinstance(game.get_actor(new_x, new_y), Key):
                game.player.has_key = True
                game.remove_actor(game.get_actor(new_x, new_y))
                self.x = new_x
                self.y = new_y
            # check if player is trying to move onto a bomb
            elif isinstance(game.get_actor(new_x, new_y), Bomb):
                if game.player.shields > 0:
                    game.player.shields -= 1
                    print(
                        "you now have " + str(game.player.shields) + " shields")
                    game.remove_actor(game.get_actor(new_x, new_y))
                else:
                    game.game_over()

            # Check if player is trying to pickup a star
            elif isinstance(game.get_actor(new_x, new_y), Star):
                self._stars_collected += 1
                game.remove_actor(game.get_actor(new_x, new_y))

            # check if the player is trying to move into a box
            elif isinstance(game.get_actor(new_x, new_y), Box):
                if game.get_actor(new_x, new_y).be_pushed(game, dx, dy):
                    self.x = new_x
                    self.y = new_y
                else:
                    new_x = self.x
                    new_y = self.y

            # check if the player is trying to open the door
            elif isinstance(game.get_actor(new_x, new_y), Door):
                if game.door_open():
                    self.x = new_x
                    self.y = new_y

                elif not game.door_open():
                    if game.get_level() == 0:
                        print("Door won't open unless you collect enough stars")
                    if game.get_level() == 1:
                        print("Door won't open unless all the monsters are dead")
                    if game.get_level() == 2:
                        print("Door won't open until you have the key and all"
                              " monsters are dead")
                    new_x, new_y = self.x, self.y

            self.x = new_x
            self.y = new_y

# === Classes for immobile objects === #


class Star(Actor):
    """
    A class to represent a Star in the game.
    """
    x: int
    y: int
    icon: pygame.Surface

    def move(self, game: 'Game') -> None:
        """
        A Star cannot move, so do nothing.
        """

        pass


class Wall(Actor):
    """
    A class to represent a Wall in the game.
    """
    x: int
    y: int
    icon: pygame.Surface

    def move(self, game: 'Game') -> None:
        """
        A Wall cannot move, so do nothing.
        """

        pass


class Door(Actor):
    """
    A class to represent a Door in the game
    """
    x: int
    y: int
    icon: pygame.Surface

    def move(self, game: 'Game') -> None:
        """
        A Door cannot move, so do nothing
        """
        pass


class Key(Actor):
    """
    A class to represent a Key in the game.
    """
    x: int
    y: int
    icon: pygame.Surface

    def move(self, game: 'Game') -> None:
        """
        A key cannot move, so do nothing.
        """
        pass


class Bomb(Actor):
    """
    A class to represent a Bomb in the game, player dies on touch,
    unless they have a shield.
    """
    x: int
    y: int
    icon: pygame.Surface

    def move(self, game: 'Game') -> None:
        """
        a bomb cannot move, so do nothing.
        """
        pass


class Shield(Actor):
    """
    A class to represent a shield power up in the game, gives the player
    the power to kill chasers and bombs on contact. does nothing against the boss.
    """
    def move(self, game: 'Game') -> None:
        """
        A shield power up cannot move, so do nothing.
        """
        pass

    def apply_power_up(self, game: 'Game'):
        """
        gives the player a shield, so when they come in contact with a chaser or
        bomb, instead of dying, they destroy it, and lose 1 shield,
        also tells the player how many shields they currently have,
        after picking one up
        """
        game.player.shields += 1
        print("you now have " + str(game.player.shields) + " shields")


# === Classes for movable objects === #


class Box(Actor):
    """
    A class to represent a box in the game
    """
    x: int
    y: int
    icon: pygame.Surface

    def move(self, game: 'Game') -> None:
        """
        A box cannot move on its own, so do nothing
        """
        pass

    def be_pushed(self, game: 'Game', dx: int, dy: int) -> bool:
        """Move the box in the direction that it is being pushed,
        represented by <dx> and <dy> if the way is not blocked by a wall.
        If there is another box in the way, move both boxes at once.
        If there is a monster in the way, squish the monster.
        Return True if a move was possible, and False otherwise."""

        if isinstance(game.get_actor(self.x + dx, self.y + dy), (Wall, Door)):
            return False
        elif not isinstance(game.get_actor(self.x + dx, self.y + dy),
                            (Wall, Box, SquishyMonster)):
            self.x += dx
            self.y += dy
            return True
        elif isinstance(game.get_actor(self.x + dx, self.y + dy), SquishyMonster):
            game.get_actor(self.x + dx, self.y + dy).die(game)
            self.x += dx
            self.y += dy
            return True
        else:
            if game.get_actor(self.x + dx, self.y + dy).be_pushed(game, dx, dy):
                self.x += dx
                self.y += dy
                return True

# === Classes for monsters === #


class Monster(Actor):
    """
    A class to represent monsters that kill the player upon contact.
    """
    # === Private attributes ===
    # _dx:
    #   the horizontal distance this monster will move during each step
    # _dy:
    #   the vertical distance this monster will move during each step
    # _delay:
    #   the speed the monster moves at
    # _delay_count:
    #   used to keep track of the monster's delay in speed
    x: int
    y: int
    icon: pygame.Surface
    _dx: float
    _dy: float
    _delay: int
    _delay_count: int

    def __init__(self, icon_file: str, x: int, y: int, dx: float, dy: float) -> None:
        """Initalize a monster with the given <icon_file> as its image,
        <x> and <y> as its position, and <dx> and <dy> being how much
        it moves by during each animation in the game. The monster also
        has a delay which could optionally be used to slow it down."""

        super().__init__(icon_file, x, y)
        self._dx = dx
        self._dy = dy
        self._delay = 5
        self._delay_count = 1

    def move(self, game: 'Game') -> None:
        """Move the monster by taking one step in its animation."""

        raise NotImplementedError

    def check_player_death(self, game: 'Game') -> None:
        """Make the game over if this monster has hit the player."""

        # check to see if player is already dead,
        # then check if they should be killed
        if not game.player:
            game.game_over()
        elif game.player.x == self.x and game.player.y == self.y:
            game.game_over()


class GhostMonster(Monster):
    """
    A class to represent a ghost in the game who chases the Player.
    """
    x: int
    y: int
    icon: pygame.Surface
    _dx: float
    _dy: float
    _delay: int
    _delay_count: int

    def __init__(self, icon_file: str, x: int, y: int) -> None:
        """Initialize a ghost with the given <icon_file> and <x> and <y>
        as its position."""

        # Set movement with each animation to be 0.5
        super().__init__(icon_file, x, y, 0.5, 0.5)  # uses Monster.__init__

    def move(self, game: 'Game') -> None:
        """
        Move the ghost on the <game>'s screen based on the player's location.
        Check if the ghost has caught the player after each move.
        """
        # added check to make sure that player exists
        if game.player:
            if game.player.x > self.x:
                self.x += self._dx
            elif game.player.x < self.x:
                self.x -= self._dx
            elif game.player.y > self.y:
                self.y += self._dy
            elif game.player.y < self.y:
                self.y -= self._dy

        self.check_player_death(game)

    def check_player_death(self, game: 'Game') -> None:
        """Make the game over if this monster has hit the player.
        for level 2, also check if the player has a shield before ending the game,
        if they do have a shield, remove that Monster"""

        # check to see if player is already dead,
        # then check if they should be killed
        if not game.player:
            game.game_over()
        elif game.player.x == self.x and game.player.y == self.y:
            # this check is for level 2, doesnt matter in other levels
            # since game.player.shields will be 0.
            if game.player.shields == 0:
                game.game_over()
            else:
                game.player.shields -= 1
                print("you now have " + str(game.player.shields) + " shields")
                game.num_chasers -= 1
                game.remove_actor(self)


class SquishyMonster(Monster):
    """
    A class to represent a monster in the game that can kill the player, or
    get squished by a box.
    """
    x: int
    y: int
    icon: pygame.Surface
    _dx: float
    _dy: float
    _delay: int
    _delay_count: int

    def __init__(self, icon_file: str, x: int, y: int) -> None:
        """Initialize a monster with the given <icon_file> and <x> and <y>
        as its position."""

        # Set movement with each animation to be 1 step
        super().__init__(icon_file, x, y, 1, 1)  # uses Monster.__init__

    def move(self, game: 'Game') -> None:
        """
        Move one step, if possible. If the way is blocked, bounce back in
        the opposite direction. After each move, check if the player has been
        hit.
        """

        if self._delay_count == 0:  # delay the monster's movement

            if isinstance(game.get_actor(self.x + self._dx, self.y + self._dy),
                          (Wall, Box, Door)):
                self._dx = -1 * self._dx
                self._dy = -1 * self._dy

            else:
                self.x += self._dx
                self.y += self._dy

        self._delay_count = (self._delay_count + 1) % self._delay

        self.check_player_death(game)

    def die(self, game: 'Game') -> None:
        """Remove this monster from the <game>."""

        game.remove_actor(self)
        game.monster_count -= 1


class BossMonster(Monster):
    """
    A class to represent a BossMonster that the player must kill,
    by touching the boss after picking up the shield power up.
    When the boss dies all the bombs and chasers are destroyed.
    """

    def __init__(self, icon_file: str, x: int, y: int) -> None:
        """Initialize a monster with the given <icon_file> and <x> and <y>
        as its position."""

        super().__init__(icon_file, x, y, 1, 1)

    def move(self, game: 'Game') -> None:
        """
        Chase the player, can move through everything except walls.
        """
        if game.player:
            if game.player.x > self.x:
                if not isinstance(game.get_actor(self.x + self._dx, self.y), Wall):
                    self.x += self._dx
            elif game.player.x < self.x:
                if not isinstance(game.get_actor(self.x - self._dx, self.y), Wall):
                    self.x -= self._dx
            elif game.player.y > self.y:
                if not isinstance(game.get_actor(self.x, self.y + self._dy), Wall):
                    self.y += self._dy
            elif game.player.y < self.y:
                if not isinstance(game.get_actor(self.x, self.y - self._dy), Wall):
                    self.y -= self._dy

        self.check_player_death(game)

    def spawn_bombs(self, game: 'Game') -> None:
        """
        the boss can spawn 2 bombs every 5 seconds,
        up to a maximum of 10 bombs.
        bombs kill the player on contact, unless he has a shield.
        """
        # the number of bombs that have been spawned max of 2 per call
        curr_bombs = 0
        if game.get_num_bombs() < 10:
            while curr_bombs < 2:
                x = random.randrange(game.stage_width)
                y = random.randrange(game.stage_height)
                if not isinstance(game.get_actor(x, y), Actor):
                    game.add_actor(Bomb("../images/bomb-24.png", x, y))
                    game.num_bombs += 1
                    curr_bombs += 1

    def spawn_chaser(self, game: 'Game') -> None:
        """
        the boss can spawn a chaser every 5 seconds, up to 3 chasers
        chasers kill the player on contact
        """
        curr_chasers = 0
        if game.get_num_chasers() < 3:
            while curr_chasers < 1:
                x = random.randrange(game.stage_width)
                y = random.randrange(game.stage_height)
                if not isinstance(game.get_actor(x, y), Actor):
                    game.add_actor(GhostMonster("../images/ghost-24.png", x, y))
                    game.num_chasers += 1
                    curr_chasers += 1

    def check_player_death(self, game: 'Game') -> None:
        """Make the game over if this monster has hit the player,
        and the player has no shields. if the player has at least 1 shield and a key
        remove the BossMonster"""

        # check to see if player is already dead,
        # then check if they should be killed
        if not game.player:
            game.game_over()
        elif game.player.x == self.x and game.player.y == self.y:
            if game.player.has_key:
                game.boss = None
                game.remove_actor(self)
            else:
                game.game_over()

