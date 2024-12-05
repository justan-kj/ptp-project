from enum import Enum


class Direction(Enum):
    NORTH = [(-1, 0), "North", "N"]
    SOUTH = [(1, 0), "South", "S"]
    EAST = [(0, 1), "East", "E"]
    WEST = [(0, -1), "West", "W"]

    @property
    def offset(self):
        return self.value[0]

    @property
    def name(self):
        return self.value[1]

    @property
    def abbreviation(self):
        return self.value[2]

    @property
    def opposite(self):
        opposites = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST,
        }
        return opposites[self]

    def __str__(self):
        return self.value[1]

    def __repr__(self):
        return self.value[1]


class Position:
    def __init__(self, row, col, max_rows=100, max_cols=100):
        self.row = row
        self.col = col
        self.max_row = max_rows
        self.max_col = max_cols

    def apply_offset(self, a_direction, apply_to_self=True, magnitude=1):
        new_row = self.row + a_direction.offset[0] * magnitude
        new_col = self.col + a_direction.offset[1] * magnitude
        if apply_to_self:
            self.row = new_row
            self.col = new_col
        return Position(new_row, new_col, self.max_row, self.max_col)

    def get_coords(self):
        return self.row, self.col

    def equals(self, position2):
        return self.get_coords() == position2.get_coords()

    def __repr__(self):
        return f"{self.row},{self.col}"
