import unittest
from tkinter.tix import INTEGER

from dungeon_game.dungeon import Dungeon
from dungeon_game.game import Game
from dungeon_game.player import Player
from dungeon_game.ui import UserInterface


class TestGame(unittest.TestCase):
    def setUp(self):
        """Sets up a test game instance
        :return: None
        """
        self.game = Game("Tester")
        pass

    def testInit(self):
        """Checks that initialised values are as expected
        :return: None
        """
        self.assertIsInstance(self.game.ui, UserInterface)
        self.assertIsInstance(self.game.player, Player)
        self.assertIsInstance(self.game.dungeon, Dungeon)
        self.assertIsInstance(self.game.seed, int)


    def testStart(self):
        """Checks that messages are added to the log when game start is called
        :return: None
        """
        self.game.start()
        self.assertEqual(len(self.game.ui.log), 1)
        self.assertEqual(self.game.ui.log[0], f"The hero {self.game.player.name} arrives in the dungeon, embarking in search of a legendary treasure.")