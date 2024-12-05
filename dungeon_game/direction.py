from enum import Enum


class Direction(Enum):
    """
    The Direction class stores cardinal directions and their properties that are commonly used across classes.
    """
    NORTH = [(-1, 0), "North", "N"]
    SOUTH = [(1, 0), "South", "S"]
    EAST = [(0, 1), "East", "E"]
    WEST = [(0, -1), "West", "W"]

    @property
    def offset(self):
        """
        The coordinate offsets of the cardinal direction according to the coordinate system used in the game
        :return: A 2-tuple containing the row, col offset for the cardinal direction.
        """
        return self.value[0]

    @property
    def name(self):
        """
        The full name of the cardinal direction.
        :return: A string that is the name of the directio, e.g. "North"
        """
        return self.value[1]

    @property
    def abbreviation(self):
        """
        The initials of the cardinal direction.
        :return: A string that is the first initial of the direction, e.g. "N"
        """
        return self.value[2]

    @property
    def opposite(self):
        """
        The opposite direction of the current direction instance. e.g. If current instance is Direction.NORTH returns Direction.SOUTH
        :return: Direction instance opposite of current one.
        """
        opposites = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST,
        }
        return opposites[self]

    def __str__(self):
        """
        String representation of the direction.

        :return: same as Direction.name
        """
        return self.value[1]

    def __repr__(self):
        """
        Debug string of the direction.

        :return: same as Direction.name
        """
        return self.value[1]


class Position:
    """
    The position class represents a set of row/col coordinates in the game grid.
    It also has some utilities for navigation and comparison between Positions
    """
    def __init__(self, row, col, max_rows=100, max_cols=100):
        """Initializes the position.
        :param row: row number of the position.
        :param col: col number of the position.
        :param max_rows: max number of rows of the grid the position is on
        :param max_cols: max number of columns of the grid the position is on
        :return: None
        """
        self.row = row
        self.col = col
        self.max_row = max_rows
        self.max_col = max_cols

    def apply_offset(self, a_direction, apply_to_self=True, magnitude=1):
        """Creates a new position with coordinates modified according to the given direction and magnitude,
        with the option to apply the modifications to the current position.
        :param a_direction: the Direction to apply the offset
        :param apply_to_self: boolean indicating whether to modify the current Position offsets
        :param magnitude: max number of rows of the grid the position is on
        :return: new Position with modified coordinates
        """
        new_row = self.row + a_direction.offset[0] * magnitude
        new_col = self.col + a_direction.offset[1] * magnitude
        if apply_to_self:
            self.row = new_row
            self.col = new_col
        return Position(new_row, new_col, self.max_row, self.max_col)

    def get_coords(self):
        """Gets the row and col coordinates of the current position.

        :return: tuple of row and col coordinates
        """
        return self.row, self.col

    def equals(self, position2):
        """Checks whether the row/col coordinates are equal to those of the given position.
        :return: boolean indicating whether the row/col coordinates are equal
        """
        return self.get_coords() == position2.get_coords()

    def __repr__(self):
        """Debug representation of the position.
        :return: string displaying row,col coordinates
        """
        return f"{self.row},{self.col}"
