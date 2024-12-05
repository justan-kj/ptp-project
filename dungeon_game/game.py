import random

from dungeon_game.direction import Position
from dungeon_game.dungeon import Dungeon
from dungeon_game.player import Player
from dungeon_game.ui import UserInterface, Choice


def generate_seed():
    """
    Generates a random seed from 0 to 2^32
    :return: integer representing teh random seed
    """
    output = random.randint(0, 2 ** 32)
    return output

class GameContext:
    """
    Represents the state of the game, holding the different components so they can easily be passed across classes.
    """

    def __init__(self):
        """
        Actual initial values are handled by the initialize method to allow possibility of a future reset method.
        """
        self.game = None
        self.dungeon = None
        self.player = None
        self.ui = None
        self.initialize()

    def initialize(self,seed=generate_seed()):
        """
        Initializes the game state.

        """
        random.seed(seed)
        self.game = Game(self)
        self.dungeon = Dungeon((5,5),self)
        self.player = Player(Position(0,0))
        self.ui = UserInterface(self)



class Game:
    """
    Manages game flow, such as start, end and player movement.
    """
    def __init__(self, context):

        self.moves = []
        self.context = context

    def start(self):
        """
        Starts the game, presenting an opening prompt and initiating an indefinite loop
        that will break once the victory condition is reached.
        :return: None
        """
        self.context.ui.update("You, an intrepid adventurer, arrive in the dungeon, embarking in search of great treasures.")
        self.context.ui.update("Legends tell of three fantastical treasures scattered throughout the dungeon, collect them all to claim victory.")
        while True:
            self.move_player()
            if self.context.player.position.equals(self.context.dungeon.endpoint):
                self.end_game()
                break

    def end_game(self, victory=True):
        """
        End the game, giving a choice to restart the game or to exit the program.
        :return: None
        """
        if victory:
            print("Congratulations! You beat the game.")
            new_game_check = input("Play again? Y/[N]")
            if new_game_check.upper() == "Y":
                self.context.initialize()
                return
            exit()

    def move_player(self):
        """
        Coordinates player movement, the main interaction with the game. Finds available routes based on the current position,
        gives players a choice on which route to take then moves the player along that direction.
        :return: None
        """
        open_paths = self.context.dungeon.get_adjacent_areas(self.context.player.position)
        choices = self.context.ui.get_movement_choices(self.moves, open_paths)
        chosen_direction = self.context.ui.prompt_player_movement(choices, self.moves)
        self.moves.append(chosen_direction)
        self.context.player.position.apply_offset(chosen_direction)
