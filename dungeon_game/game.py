import random

from dungeon_game.direction import Position
from dungeon_game.dungeon import Dungeon
from dungeon_game.player import Player
from dungeon_game.ui import UserInterface, Choice


def generate_seed():
    output = random.randint(0,2**32)
    return output

class Game:
    def __init__(self, name, size=(5,5), seed=generate_seed()):
        self.seed = seed
        self.dungeon = Dungeon(size)
        starting_pos = Position(0,0,size[0],size[1])
        self.player = Player(name, starting_pos)
        self.ui = UserInterface()

    def start(self):
        self.ui.update(f"The hero {self.player.name} arrives in the dungeon, embarking in search of a legendary treasure.")
        while True:
            self.move_player()

    def move_player(self):
        open_paths = self.dungeon.get_adjacent_areas(self.player.position)
        choices = []
        for key in open_paths:
            if open_paths[key]:
                prompt = f"Head {key.name}wards"
                choices.append(Choice(prompt,key))
        chosen_direction = self.ui.get_choice(choices)
        self.player.position.apply_offset(chosen_direction)
        self.ui.update(f"You have moved {chosen_direction.name}wards")






