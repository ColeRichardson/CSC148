from __future__ import annotations
from typing import Optional
from actors import *
import pygame

class Game:
    """
    This class represents the main game.
    === Attributes ===
    screen: the window where the game is being played.
    stage_width: the width of the stage, the number of columns in the maze0.txt file.
    stage_height: the height of the stage, the number of rows in the maze0.txt file - 1 so we start at 0.
    size: the size of the pygame screen, where the game occurs. length and height of grid multplied by ICON_SIZE
    player: player object, holds information about the player.
    goal_stars: the number of stars the player must collect to win
    keys_pressed: holds the most recent keystroke

    == Private Attributes ==
    _running: holds the status of whether the game is running or not, True = running, False = stopped.
    _actors: holds the actors that are in the game, such as walls, stars, players, and chasers.
    """
    screen: pygame.display
    stage_width: int
    stage_height: int
    size: int
    player: player
    goal_stars: int
    keys_pressed: pygame.key

    _running: bool
    _actors: list


    def __init__(self, w, h) -> None:
        """
        Initialize a game that has a display screen and game actors.
        """

        self._running = False
        self._actors = []

        self.screen = None
        self.stage_width, self.stage_height = w, h-1
        self.size = (w * ICON_SIZE, h * ICON_SIZE)

        self.player = None
        self.goal_stars = 0

        self.keys_pressed = None

    def set_player(self, player: Player) -> None:
        """
        Set the game's player to be the given <player> object.
        """

        self.player = player

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

    def on_loop(self) -> None:
        """
        Move all actors in the game as appropriate.
        Check for win/lose conditions and stop the game if necessary.
        """

        self.keys_pressed = pygame.key.get_pressed()
        for actor in self._actors:
            actor.move(self)
        if self.player == None:
            print("You lose! :( Better luck next time.")
            self._running = False
        elif self.player.has_won(self) == True:
            print("Congratulations, you won!")
            self._running = False


    def on_render(self) -> None:
        """
        Render all the game's elements onto the screen.
        """

        self.screen.fill(BLACK)
        for a in self._actors:
            rect = pygame.Rect(a.x * ICON_SIZE, a.y * ICON_SIZE, ICON_SIZE, ICON_SIZE)
            self.screen.blit(a.icon, rect)

        font = pygame.font.Font('freesansbold.ttf', 12)
        text = font.render('Objective: Collect 5 stars before the ' + \
                           'ghost gets you', True, WHITE, BLACK)
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
