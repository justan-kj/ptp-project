
from dungeon_game.area import Area
from dungeon_game.maze_builder import MazeBuilder
from dungeon_game.direction import Direction, Position

def check_path(area1, area2):
    for direction in Direction:
        if area1.exits[direction] == area2.exits[direction.opposite]:
            return True
    return False

class Dungeon:
    """The Dungeon class manages the structure and relationships of areas in the game map"""
    def __init__(self, size, player):
        """Initializes the dungeon.
        :param size: a 2-tuple of the form (rows, columns)
        :return: None
        """
        self.size = size
        rows,cols = size
        self.areas = MazeBuilder(size, player).build_maze()
        self.endpoint = Position(size[0]-1,size[1]-1,rows,cols)

    def get_area(self, position):
        """get_area returns an area from self.areas based on its row and column."""
        return self.areas[position.row][position.col]

    def get_adjacent_areas(self, area_position):
        """get_adjacent_areas returns the adjacent areas of a target area contained in self.areas. the target area is identified by its row and column."""
        adjacent_areas = {}
        for a_dir in Direction:
            new_pos = area_position.apply_offset(a_dir, False)
            new_row,new_col = new_pos.get_coords()
            if new_row < 0 or new_row >= self.size[0] or new_col < 0 or new_col >= self.size[1]:
                adjacent_areas[a_dir] = False
                continue
            if check_path(self.get_area(area_position), self.get_area(new_pos)):
                adjacent_areas[a_dir] = self.get_area(new_pos)
            else:
                adjacent_areas[a_dir] = False
        return adjacent_areas



