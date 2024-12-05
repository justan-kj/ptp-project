from dungeon_game.direction import Direction, Position
from dungeon_game.maze_builder import MazeBuilder


def check_path(area1, area2, direction):
    """
    Checks that 2 areas have the linked exits. Exits are considered linked if an open directional exit in area1 has
    the corresponding opposite direction exit open in area 2. Area1 and area2 are assumed to be adjacent and
    the direction is assumed to reflect their adjacency.

    :param area1: an Area
    :param area2: an adjacent Area to the first
    :param direction: a direction going from area1 towards area2
    :return: bool indicating if the 2 areas have linked exits in the given direction
    """
    return area1.exits[direction] and area1.exits[direction] == area2.exits[direction.opposite]

class Dungeon:
    """The Dungeon class manages the structure and relationships of areas in the game map"""

    def __init__(self, size):
        """Initializes the dungeon.
        :param size: a 2-tuple of the form (rows, columns)
        :return: None
        """
        self.size = size
        rows, cols = size
        self.areas = MazeBuilder(size).build_maze()
        self.endpoint = Position(size[0] - 1, size[1] - 1, rows, cols)

    def get_area(self, position):
        """Gets a dungeon area from its position   .
        :param position: the Position of the area to be returned
        :return: Area of the dungeon
        """
        return self.areas[position.row][position.col]

    def get_adjacent_areas(self, area_position):
        """Gets areas in self.area that are adjacent to the target area and have linked exits.
            :param area_position: the Position of the area whose adjacent areas need finding
            :return: array of adjacent areas with linked exits
        """
        adjacent_areas = {}
        for a_dir in Direction:
            new_pos = area_position.apply_offset(a_dir, False)
            new_row, new_col = new_pos.get_coords()
            if new_row < 0 or new_row >= self.size[0] or new_col < 0 or new_col >= self.size[1]:
                adjacent_areas[a_dir] = False
                continue
            if check_path(self.get_area(area_position), self.get_area(new_pos),a_dir):
                adjacent_areas[a_dir] = self.get_area(new_pos)
            else:
                adjacent_areas[a_dir] = False
        return adjacent_areas
