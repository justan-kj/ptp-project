import unittest
from ctypes.wintypes import POINT

from dungeon_game.direction import Position, Direction


class TestPosition(unittest.TestCase):
    def setUp(self):
        """Sets up a test player named Chuck Tester using defaults for other params
        :return: None
        """
        self.position = Position(3,4)

    def test_init(self):
        """Checks that initialised values are as expected
        :return: None
        """
        self.assertEqual(self.position.row, 3)
        self.assertEqual(self.position.col, 4)
        self.assertEqual(self.position.max_row, 100)
        self.assertEqual(self.position.max_col, 100)

    def test_offset_self(self):
        self.position.apply_offset(Direction.NORTH)
        self.assertEqual(self.position.row, 2)
        self.assertEqual(self.position.col, 4)

    def test_offset_new(self):
        new_position = self.position.apply_offset(Direction.WEST, False)
        self.assertEqual(new_position.row, 3)
        self.assertEqual(new_position.col, 3)

    def test_offset_magnitude(self):
        self.position.apply_offset(Direction.NORTH, True, 3)
        self.assertEqual(self.position.row, 0)
        self.assertEqual(self.position.col, 4)

    def test_repr(self):
        self.assertEqual(repr(self.position), "3,4")

    def test_get_coords(self):
        self.assertEqual(self.position.get_coords(), (3, 4))

    def test_equals(self):
        pos1 = self.position
        pos2 = Position(3,4)
        pos3 = Position(4, 4)
        self.assertTrue(pos1.equals(pos2))
        self.assertFalse(pos1.equals(pos3))
        self.assertFalse(pos2.equals(pos3))

class TestDirection(unittest.TestCase):
    def test_offset(self):
        self.assertEqual(Direction.NORTH.offset, (-1,0))
        self.assertEqual(Direction.SOUTH.offset, (1, 0))
        self.assertEqual(Direction.EAST.offset, (0, 1))
        self.assertEqual(Direction.WEST.offset, (0, -1))

    def test_opposite(self):
        self.assertEqual(Direction.NORTH.opposite, Direction.SOUTH)
        self.assertEqual(Direction.EAST.opposite, Direction.WEST)

    def test_abbreviation(self):
        self.assertEqual(Direction.NORTH.abbreviation, "N")
        self.assertEqual(Direction.EAST.abbreviation, "E")

    def test_name(self):
        self.assertEqual(Direction.SOUTH.name, "South")
        self.assertEqual(Direction.WEST.name, "West")