import random

from dungeon_game.direction import Position
from dungeon_game.dungeon import Dungeon
from dungeon_game.player import Player
from dungeon_game.ui import UserInterface, Choice


def generate_seed():
    output = random.randint(0, 2 ** 32)
    return output

class GameContext:

    def __init__(self):
        self.seed = 0
        self.game = None
        self.dungeon = None
        self.player = None
        self.ui = None
        self.initialize()

    def initialize(self,seed=generate_seed()):
        self.seed = seed
        self.game = Game(self)
        self.dungeon = Dungeon((5,5),self)
        self.player = Player(Position(0,0))
        self.ui = UserInterface(self)


class Game:
    def __init__(self, context):
        self.moves = []
        self.context = context

    def start(self):
        self.context.ui.update(
            f"You arrive in the dungeon, embarking in search of a legendary treasure.")
        while True:
            self.move_player()
            if self.context.player.position.equals(self.context.dungeon.endpoint):
                break

    def end_game(self, victory=True):
        if victory:
            print("Congratulations! You beat the game.")
            new_game_check = input("Play again? Y/[N]")
            if new_game_check.upper() == "Y":
                self.context.initialize()
            exit()

    def move_player(self):
        open_paths = self.context.dungeon.get_adjacent_areas(self.context.player.position)
        choices = self.context.ui.get_movement_choices(self.moves, open_paths)
        chosen_direction = self.context.ui.prompt_player_movement(choices, self.moves)
        self.moves.append(chosen_direction)
        self.context.player.position.apply_offset(chosen_direction)
