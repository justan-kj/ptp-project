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

    def test_generate_path(self):
        with patch('random.shuffle') as mock_shuffle:
            mock_shuffle.side_effect = lambda x: x  # Prevent shuffling for predictability
            maze = self.builder.initialize_maze()
            self.builder.generate_maze_path()

            # Count the number of passages; for a 4x4 maze, it should have 16 - 1 = 15 passages
            passage_count = 0
            for row in maze:
                for area in row:
                    passage_count += sum(area.exits.values())
            self.assertEqual(passage_count, 30)  # Each passage is counted twice

            # Additionally, verify that all areas are connected
            visited = set()
            stack = [maze[0][0]]
            while stack:
                current = stack.pop()
                if current in visited:
                    continue
                visited.add(current)
                for direction, exists in current.exits.items():
                    if exists:
                        if direction == Direction.NORTH:
                            neighbor = maze[current.position.row - 1][current.position.col]
                        elif direction == Direction.SOUTH:
                            neighbor = maze[current.position.row + 1][current.position.col]
                        elif direction == Direction.EAST:
                            neighbor = maze[current.position.row][current.position.col + 1]
                        elif direction == Direction.WEST:
                            neighbor = maze[current.position.row][current.position.col - 1]
                        if neighbor not in visited:
                            stack.append(neighbor)
            self.assertEqual(len(visited), 16)  # All 16 areas should be visited
