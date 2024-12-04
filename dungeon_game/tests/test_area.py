import unittest
from dungeon_game.area import Area
from dungeon_game.direction import Direction,Position

class TestArea(unittest.TestCase):
    def setUp(self):
        """Sets up a test area
        :return: None
        """
        self.area = Area(Position(1,2,10,10))

    def test_init(self):
        """Checks that initialised values are as expected
        :return: None
        """

        for key in Direction:
            self.assertIn(key,self.area.exits)
            self.assertFalse(self.area.exits[key])
        self.assertEqual(self.area.row, 1)
        self.assertEqual(self.area.col, 2)
