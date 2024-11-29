
from dungeon_game.area import Area
from dungeon_game.maze_builder import MazeBuilder
class Dungeon:
    """The Dungeon class manages the structure and relationships of areas in the game map"""
    def __init__(self, size):
        """Initializes the dungeon.
        :param size: a 2-tuple of the form (rows, columns)
        :return: None
        """
        self.size = size
        self.areas = MazeBuilder(size).build

    def get_area(self, row,col):
        """get_area returns an area from self.areas based on its row and column."""
        return self.areas[row][col]

    def get_adjacent_areas(self, target_row,target_col):
        """get_adjacent_areas returns the adjacent areas of a target area contained in self.areas. the target area is identified by its row and column."""
        adjacent_areas = {}
        offsets = [(1, 0), (-1,0), (0,1), (0,-1)]
        offset_labels = ["N", "S", "E", "W"]
        for id, offset in enumerate(offsets):
            new_row,new_col = target_row + offset[0], target_col + offset[1]
            if new_row < 0 or new_row >= self.size[0] or new_col < 0 or new_col >= self.size[1]:
                adjacent_areas[offset_labels[id]] = False
                continue
            if check_path(self.get_area(target_row,target_col), self.get_area(new_row, new_col)):
                adjacent_areas[offset_labels[id]] = self.get_area(new_row, new_col)
            else:
                adjacent_areas[offset_labels[id]] = False
        return adjacent_areas

