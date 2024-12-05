import unittest

from dungeon_game.direction import Position, Direction
from dungeon_game.map import Map
from dungeon_game.area import Area
from dungeon_game.maze_builder import link_areas
from dungeon_game.ui import UserInterface


class TestMap(unittest.TestCase):
    def setUp(self):
        """Sets up a test game instance
        :return: None
        """
        self.areas = [
            [Area(Position(0,0)),
            Area(Position(0, 1))],
            [Area(Position(1, 0)),
            Area(Position(1, 1))],
        ]
        link_areas(self.areas[0][0], self.areas[1][0], Direction.SOUTH)
        link_areas(self.areas[0][0], self.areas[0][1], Direction.EAST)
        link_areas(self.areas[1][0], self.areas[1][1], Direction.EAST)


    def test_display(self):
        """Checks that initialised values are as expected
        :return: None
        """
        test_map = Map(self.areas)
        test_map.display()
        pass



"""Checks that messages are added to the log when game start is called
        :return: None
        """
"""    def testStart(self):
        
        self.game.start()
        self.assertEqual(len(self.game.ui.log), 1)
        self.assertEqual(self.game.ui.log[0], f"The hero {self.game.player.name} arrives in the dungeon, embarking in search of a legendary treasure.")"""
