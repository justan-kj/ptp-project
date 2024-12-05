import unittest
from dungeon_game.event import BlankEvent
from dungeon_game.direction import Direction, Position
from dungeon_game.player import Player


class TestBlankEvent(unittest.TestCase):
    def setUp(self):
        """Sets up a test area
        :return: None
        """
        self.player = Player(Position(0, 0))
        self.event = BlankEvent(self.player)

    def test_init(self):
        """Checks that initialised values are as expected
        :return: None
        """

        self.assertTrue(self.event.active)
        self.assertEqual(self.event.description, "Nothing eventful happens along the way.")

    def test_activate(self):
        self.assertEqual(self.event.activate(), "Nothing eventful happens along the way.")
