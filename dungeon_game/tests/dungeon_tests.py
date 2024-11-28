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
        self.dungeon = Dungeon(self.size)

    def test_init(self):
        """Checks that initialised values are as expected
        :return: None
        """
        rows,cols = self.size
        self.assertEqual(len(self.dungeon.areas), rows)
        self.assertEqual(len(self.dungeon.areas[0]), cols)
        self.assertTrue(all_items_are_type(self.dungeon.areas, Area))

    def test_pathing(self):
        """Checks that the generate_path functions produces an expected path
        :return: None
        """
        self.assertIsInstance(self.dungeon.generate_path((0,0)), Area)
        rows, cols = self.size
        for col in range(cols - 1):
            self.assertTrue(self.dungeon.areas[0][col].exits["E"])
            if col>0:
                self.assertTrue(self.dungeon.areas[0][col].exits["W"])
        self.assertTrue(self.dungeon.areas[0][cols - 1].exits["W"])

    def test_get_area(self):
        """Checks that get_area returns the correct area
        :return: None
        """
        area = self.dungeon.get_area(2, 3)
        self.assertIsInstance(area, Area)
        self.assertEqual(area, self.dungeon.areas[2][3])

    def test_get_adjacent_areas(self):
        """Checks that get_adjacent_areas returns correctly linked areas
        :return: None
        """
        start_row, start_col = 0, 0
        self.dungeon.generate_path((start_row, start_col))
        adjacent = self.dungeon.get_adjacent_areas(start_row, start_col)

        # The East area should be valid
        self.assertIsInstance(adjacent["E"], Area)

        # The other directions should not be connected yet
        self.assertFalse(adjacent["N"])
        self.assertFalse(adjacent["S"])
        self.assertFalse(adjacent["W"])

    def test_bridge_areas(self):
        """Checks that bridge_areas correctly links two areas
        :return: None
        """
        area1 = self.dungeon.areas[0][0]
        area2 = self.dungeon.areas[0][1]
        bridge_areas(area1, area2)
        self.assertTrue(area1.exits["E"])
        self.assertTrue(area2.exits["W"])

    def test_check_path(self):
        """Checks that check_path correctly identifies linked areas
        :return: None
        """
        area1 = self.dungeon.areas[0][0]
        area2 = self.dungeon.areas[0][1]
        area3 = self.dungeon.areas[1][3]

        # Link area1 and area2
        bridge_areas(area1, area2)

        # Validate paths
        self.assertTrue(check_path(area1, area2))
        self.assertFalse(check_path(area2, area3))
