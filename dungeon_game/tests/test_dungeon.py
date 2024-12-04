import unittest
from dungeon_game.dungeon import *
from dungeon_game.area import Area

def all_items_are_type(a_2d_list,a_type):
    """checks if all items in a list are of a particular type
        :param a_2d_list: a 2d list to check
        :param a_type: the type to check each list element against
        :return: boolean, True if all items are of a_type, otherwise False
    """
    for row in a_2d_list:
        for ele in row:
            if not isinstance(ele,a_type) and ele is not None:
                return False
    return True

class TestDungeon(unittest.TestCase):
    def setUp(self):
        """Sets up a test dungeon of size (4,5)
        :return: None
        """
        self.size = (4,5)
        self.seed = 1050066143
        self.dungeon = Dungeon(self.size, self.seed)

    def test_init(self):
        """Checks that initialised values are as expected
        :return: None
        """
        rows,cols = self.size
        self.assertEqual(len(self.dungeon.areas), rows)
        self.assertEqual(len(self.dungeon.areas[0]), cols)
        self.assertTrue(all_items_are_type(self.dungeon.areas, Area))


    def test_get_area(self):
        """Checks that get_area returns the correct area
        :return: None
        """
        area = self.dungeon.get_area(Position(2,3))
        self.assertIsInstance(area, Area)
        self.assertEqual(area, self.dungeon.areas[2][3])

    def test_get_adjacent_areas(self):
        """Checks that get_adjacent_areas returns correctly linked areas
        :return: None
        """
        adjacent = self.dungeon.get_adjacent_areas(Position(0,0,4,5))

        # The East area should be valid
        self.assertIsInstance(adjacent[Direction.EAST], Area)
        self.assertIsInstance(adjacent[Direction.SOUTH], Area)

        # The other directions should not be connected yet
        self.assertFalse(adjacent[Direction.NORTH])
        self.assertFalse(adjacent[Direction.WEST])
