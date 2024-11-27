
from dungeon_game.area import Area

def bridge_areas(area1,area2):
    area1.exits["E"] = True
    area2.exits["W"] = True
    return area2

class Dungeon():
    """The Dungeon class represents the space the player passes through.
    It contains the areas a player can move through"""
    def __init__(self, size):
        """Initializes the dungeon.
        :param size: a 2-tuple of the form (rows, columns)
        :return: None
        """
        self.size = size
        rows, cols = size
        self.areas = [[Area() for _ in range(cols)] for _ in range(rows)]

    def generate_path(self, starting_point):
        start_row,start_col = starting_point
        rows, cols = self.size
        current_col = start_col
        while current_col < cols - 1:
            bridge_areas(self.areas[start_row][current_col], self.areas[start_row][current_col + 1])
            current_col += 1
        return self.areas[start_row][current_col]

