import unittest

from dungeon_game.area import Area
from dungeon_game.direction import Position, Direction
from dungeon_game.game import GameContext
from dungeon_game.maze_builder import MazeBuilder


class TestMazeBuilder(unittest.TestCase):
    def setUp(self):
        self.context = GameContext()
        self.size = (12,34)
        self.builder = MazeBuilder(self.size,self.context)

    def test_init(self):
        self.assertEqual(self.builder.rows, self.size[0])
        self.assertEqual(self.builder.cols, self.size[1])
        self.assertIsNone(self.builder.maze)


    def test_build_empty_maze(self):
        maze = self.builder.initialize_maze()
        self.assertEqual(len(maze), self.size[0])  # 4 rows
        for row_idx, row in enumerate(maze):
            self.assertEqual(len(row), self.size[1])  # 4 columns per row

    def test_bridge_areas(self):
        area1 = Area(Position(2, 3))
        area2 = Area(Position(2, 4))
        self.builder.link_areas(area1, area2, Direction.EAST)

        self.assertTrue(area1.exits[Direction.EAST])
        self.assertTrue(area2.exits[Direction.WEST])

        self.assertFalse(area1.exits[Direction.NORTH])
        self.assertFalse(area1.exits[Direction.SOUTH])
        self.assertFalse(area1.exits[Direction.WEST])
        self.assertFalse(area2.exits[Direction.NORTH])
        self.assertFalse(area2.exits[Direction.SOUTH])
        self.assertFalse(area2.exits[Direction.EAST])

