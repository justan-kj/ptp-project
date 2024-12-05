import unittest

from dungeon_game.area import Area
from dungeon_game.direction import Position, Direction
from dungeon_game.maze_builder import MazeBuilder


class TestMazeBuilder(unittest.TestCase):
    def setUp(self):
        self.size = (4, 4)
        self.seed = 1050066143
        self.builder = MazeBuilder(self.size, self.seed)

    def test_init(self):
        self.assertEqual(self.builder.rows, 4)
        self.assertEqual(self.builder.cols, 4)
        self.assertIsNone(self.builder.maze)
        self.assertEqual(self.builder.seed, 1050066143)

    def test_build_empty_maze(self):
        maze = self.builder.initialize_maze()
        self.assertEqual(len(maze), 4)  # 4 rows
        for row_idx, row in enumerate(maze):
            self.assertEqual(len(row), 4)  # 4 columns per row

    def test_bridge_areas(self):
        area1 = Area(Position(0, 0))
        area2 = Area(Position(0, 1))
        self.builder.link_areas(area1, area2, Direction.EAST)
        self.assertTrue(area1.exits[Direction.EAST])
        self.assertTrue(area2.exits[Direction.WEST])
