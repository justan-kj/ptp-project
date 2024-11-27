import random
from dungeon_game.dungeon import Dungeon
from dungeon_game.player import Player
from dungeon_game.ui import UserInterface


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



