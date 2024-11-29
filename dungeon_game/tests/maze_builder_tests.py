import unittest
from dungeon_game.maze_builder import MazeBuilder

class TestMazeBuilder(unittest.TestCase):


    def testBuild(self):
        """Checks that messages are added to the log when game start is called
        :return: None
        """
        m = MazeBuilder((3, 3))
        empty_maze = m.build_empty_maze()
        self.assertEqual(len(empty_maze), 3)
        self.assertEqual(len(empty_maze[0]), 3)
        m.generate_path()
        print(m.maze)