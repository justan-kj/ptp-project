import unittest
from dungeon_game.dungeon import Dungeon
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