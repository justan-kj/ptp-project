import unittest
from dungeon_game.dungeon import Dungeon
from dungeon_game.game import Game
from dungeon_game.player import Player
from dungeon_game.ui import UserInterface


class TestGame(unittest.TestCase):
    def setUp(self):
        """Sets up a test game instance
        :return: None
        """
        pass

    def testInit(self):
        """Checks that initialised values are as expected
        :return: None
        """
        pass


"""Checks that messages are added to the log when game start is called
        :return: None
        """
"""    def testStart(self):
        
        self.game.start()
        self.assertEqual(len(self.game.ui.log), 1)
        self.assertEqual(self.game.ui.log[0], f"The hero {self.game.player.name} arrives in the dungeon, embarking in search of a legendary treasure.")"""
