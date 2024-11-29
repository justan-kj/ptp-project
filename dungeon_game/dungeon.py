
from dungeon_game.area import Area

def bridge_areas(area1,area2):
    """
    The bridge_areas function enables an exit for area1 and the corresponding exit for area2
    """
    area1.exits["E"] = True
    area2.exits["W"] = True
    return area2

def check_path(area1, area2):
    """
    The check_path function checks whether there are linked exits between area1 and area2
    """
    pairs = [("N", "S"), ("S", "N"), ("E", "W"), ("W", "E")]
    for pair in pairs:
        if area1.exits[pair[0]] and area2.exits[pair[1]]:
            return True
    return False


class Dungeon():
    """The Dungeon class manages the structure and relationships of areas in the game map"""
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

