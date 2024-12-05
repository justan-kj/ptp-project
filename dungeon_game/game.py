import random

from dungeon_game.direction import Position
from dungeon_game.dungeon import Dungeon
from dungeon_game.player import Player
from dungeon_game.ui import UserInterface, Choice


def generate_seed():
    output = random.randint(0, 2 ** 32)
    return output


class Game:
    def __init__(self, name=None):
        self.dungeon = None
        self.player = None
        self.seed = 0
        self.ui = None
        self.moves = []
        self.initialize(name)

    def initialize(self):
        size = (5, 5)
        self.seed = generate_seed()
        starting_pos = Position(0, 0, size[0], size[1])
        self.player = Player(starting_pos)
        self.dungeon = Dungeon(size, self.player)
        self.ui = UserInterface()

    def start(self):
        self.ui.update(
            f"You arrive in the dungeon, embarking in search of a legendary treasure.")
        while True:
            self.move_player()
            if self.player.position.equals(self.dungeon.endpoint):
                break

    def end_game(self, victory=True):
        if victory:
            print("Congratulations! You beat the game.")
            new_game_check = input("Play again? Y/[N]")
            if new_game_check.upper() == "Y":
                self.initialize()
            exit()

    def move_player(self):
        open_paths = self.dungeon.get_adjacent_areas(self.player.position)
        choices = []
        back_direction = None
        is_first_move = len(self.moves) == 0
        for key in open_paths:
            if not is_first_move and key == self.moves[-1].opposite:
                back_direction = key
                continue
            if open_paths[key]:
                prompt = f"Move {key.name}"
                choices.append(Choice(prompt, key))
        if back_direction:
            choices.append(Choice(f"Go back ({back_direction.name})", back_direction))

        chosen_direction = self.ui.get_choice(choices, is_first_move)
        self.moves.append(chosen_direction)
        self.ui.update(f"You move towards the {chosen_direction.name}")
        event = self.dungeon.get_area(self.player.position).exits[chosen_direction]
        event.activate()
        self.player.position.apply_offset(chosen_direction)
