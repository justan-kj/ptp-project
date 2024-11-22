import unittest
from dungeon_game.area import Area

class TestArea(unittest.TestCase):
    def setUp(self):
        """Sets up a test area
        :return: None
        """
        self.area = Area()

    def test_init(self):
        """Checks that initialised values are as expected
        :return: None
        """
        exit_keys = ['N','S','E','W']
        for key in exit_keys:
            self.assertIn(key,self.area.exits)
            self.assertFalse(self.area.exits[key])