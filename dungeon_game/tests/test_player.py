import unittest
from dungeon_game.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        """Sets up a test player named Chuck Tester using defaults for other params
        :return: None
        """
        self.player = Player("Chuck Tester")

    def test_init(self):
        """Checks that initialised values are as expected
        :return: None
        """
        self.assertEqual(self.player.name, "Chuck Tester")
        self.assertEqual(self.player.max_hp, 100)
        self.assertEqual(self.player.current_hp, 100)
        self.assertEqual(self.player.position, (0,0))