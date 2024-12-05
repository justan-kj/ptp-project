import random

from dungeon_game.direction import Position
from dungeon_game.dungeon import Dungeon
from dungeon_game.inventory import Item
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
        """
        Initializes the game with ab empty record of moves taken and the game state.
        :return: None
        """
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
        treasures = self.assign_items()
        while not self.check_victory(treasures):
            self.move_player()
        self.end_game()

    def assign_items(self):
        """
        Creates and assigns items to areas. Currently set to the 3 non-starting corners. Player wins the game by collecting all 3.
        :return: array of Items that were assigned to areas
        """
        dungeon_areas = self.context.dungeon.areas
        max_row,max_col = len(dungeon_areas) - 1, len(dungeon_areas[0]) - 1
        item1 = Item("QuickestSort Algorithm", "Sorts an array in O(-1) time.")
        dungeon_areas[0][max_col].add_item(item1)
        item2 = Item("Orange Apple", "Quite comparable to both.")
        dungeon_areas[max_row][0].add_item(item2)
        item3 = Item("Free Lunch", "Turns out there is such a thing after all.")
        dungeon_areas[max_row][max_col].add_item(item3)
        return [item1, item2, item3]

    def check_victory(self, items_to_check):
        """
        Checks if all the required items are in the player's inventory.
        :param items_to_check: array of Items to check
        :return: boolean indicating if all items are present in the player's inventory'
        """
        for item in items_to_check:
            if not item in self.context.player.inventory:
                return False
        return True

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
