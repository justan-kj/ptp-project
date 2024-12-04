import random

from dungeon_game.direction import Position
from dungeon_game.dungeon import Dungeon
from dungeon_game.player import Player
from dungeon_game.ui import UserInterface, Choice
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def generate_seed():
    output = random.randint(0,2**32)
    return output

class Game:
    def __init__(self, name=None):
        self.dungeon = None
        self.player = None
        self.seed = 0
        self.ui = None
        self.moves = []
        self.initialize(name)

    def initialize(self,player_name=None):
        if player_name is None:
            player_name = input("Welcome to Adventure world, please enter your character's name: ")

        size = (5,5)
        self.seed = generate_seed()
        self.dungeon = Dungeon(size, self.seed)
        starting_pos = Position(0, 0, size[0], size[1])
        self.player = Player(player_name, starting_pos)
        self.ui = UserInterface()

    def start(self):
        self.ui.update(f"The hero {self.player.name} arrives in the dungeon, embarking in search of a legendary treasure.")
        while True:
            self.move_player()
            if self.player.position.equals(self.dungeon.endpoint):

                break
    def end_game(self,victory = True):
        if victory:
            print("Congratulations! You beat the game.")
            new_game_check = input("Play again? Y/N")
            if new_game_check.upper() == "Y":
                cls()
                self.initialize()



    def move_player(self):
        open_paths = self.dungeon.get_adjacent_areas(self.player.position)
        choices = []
        back_direction = None
        for key in open_paths:
            if len(self.moves) and key == self.moves[-1].opposite:
                back_direction = key
                continue
            if open_paths[key]:
                prompt = f"Head {key.name}wards"
                choices.append(Choice(prompt,key))
        if back_direction:
            choices.append(Choice("Go back", back_direction))
        chosen_direction = self.ui.get_choice(choices)
        self.moves.append(chosen_direction)
        self.player.position.apply_offset(chosen_direction)
        self.ui.update(f"You have moved {chosen_direction.name}wards")






