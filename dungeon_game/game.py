import random
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
        self.player = Player(name)
        self.ui = UserInterface()

    def start(self):
        self.ui.update(f"The hero {self.player.name} arrives in the dungeon, embarking in search of a legendary treasure.")
        while True:
            self.move_player()

    def move_player(self):
        current_row, current_column = self.player.position
        open_paths = self.dungeon.get_adjacent_paths(current_row, current_column)
        choices = []
        for key in open_paths:
            if open_paths[key]:
                prompt = f"Go {key}"
                choices.append(Choice(prompt,key))
        choice = self.ui.get_choice(choices)
        offsets = {"N":(1,0),"S":(-1,0),"E":(0,-1),"W":(1,0)}
        self.player.position = (current_row+offsets[choice][0],current_column+offsets[choice][1])
        self.ui.update(f"You have moved {choice}")




