import unittest
from dungeon_game.area import Area, get_symbol
from dungeon_game.direction import Direction, Position


class TestArea(unittest.TestCase):
    def setUp(self):
        """Sets up a test area
        :return: None
        """
        self.area = Area(Position(1, 2, 10, 10))

    def test_init(self):
        """Checks that initialised values are as expected
        :return: None
        """

        for key in Direction:
            self.assertIn(key, self.area.exits)
            self.assertFalse(self.area.exits[key])
        self.assertEqual(self.area.row, 1)
        self.assertEqual(self.area.col, 2)

    def test_get_symbol(self):
        test_exits = {Direction.NORTH: False, Direction.SOUTH: False,
                      Direction.EAST: False, Direction.WEST: False}
        self.assertEqual(get_symbol(test_exits), "0000")
        test_exits = {Direction.NORTH: True, Direction.SOUTH: True,
                      Direction.EAST: True, Direction.WEST: True}
        self.assertEqual(get_symbol(test_exits), "1111")
        test_exits = {Direction.NORTH: False, Direction.SOUTH: True,
                      Direction.EAST: True, Direction.WEST: True}
        self.assertEqual(get_symbol(test_exits), "1011")
        test_exits = {Direction.NORTH: True, Direction.SOUTH: False,
                      Direction.EAST: False, Direction.WEST: True}
        self.assertEqual(get_symbol(test_exits), "1100")

    def test_repr(self):
        self.area.exits[Direction.NORTH] = True
        self.area.exits[Direction.EAST] = True
        self.assertEqual(repr(self.area), "└")
        self.area.exits[Direction.EAST] = False
        self.assertEqual(repr(self.area), "╵")
        self.area.exits[Direction.WEST] = True
        self.assertEqual(repr(self.area), "┘")
