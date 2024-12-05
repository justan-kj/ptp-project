from dungeon_game.direction import Direction
from dungeon_game.area import get_symbol


class Map:
    """
    A class that manages the dungeon map, a string representation of the areas and exits in the dungeon.
    """
    def __init__(self, areas):
        """
        Initializes the map, using the provided areas to construct borders corresponding to each area
        :param areas: a list of areas in the dungeon
        :return: None
        """
        self.areas = areas
        self.borders = self.build_borders()

    def build_borders(self):
        """
        Builds the borders corresponding to each area.
        :return: a list of borders
        """
        num_rows, num_cols = len(self.areas), len(self.areas[0])
        border_rows, border_cols = num_rows * 2 + 1, num_cols * 2 + 1
        borders = [[None for col in range(border_cols)] for row in range(border_rows)]
        for row in range(border_rows):
            for col in range(border_cols):
                if row % 2 == 0 and col % 2 == 0:
                    borders[row][col] = Corner(row, col, border_rows, border_cols)
                    continue

                if col % 2 == 0:
                    borders[row][col] = Edge(1, not col > 0 and row < border_cols - 1)
                    continue
                if row % 2 == 0:
                    borders[row][col] = Edge(0, not row > 0 and row < border_rows - 1)
                else:
                    borders[row][col] = Edge(0, True)

        for row in range(num_rows):
            for col in range(num_cols):
                area = self.areas[row][col]
                b_row, b_col = row * 2, col * 2
                borders[b_row][b_col + 1].passable = area.exits[Direction.NORTH]
                borders[b_row + 1][b_col +2].passable = area.exits[Direction.EAST]
                borders[b_row + 2][b_col + 1].passable = area.exits[Direction.SOUTH]
                borders[b_row + 1][b_col].passable = area.exits[Direction.WEST]

        return borders

    def display(self):
        """
        Displays the map, using border objects to print an outline of the maze.
        :return: None
        """
        self.build_borders()
        for row in self.borders:
            line = ""
            for col in row:
                line += col.display()
            print(line)


class Corner:
    """
    Represents the border in the intersection between corners of adjacent areas.
    """
    def __init__(self, row, col, max_row, max_col):
        self.neighbours = {
            Direction.NORTH: row > 0,
            Direction.SOUTH: row < max_row - 1,
            Direction.EAST: col < max_col - 1,
            Direction.WEST: col > 0,
        }

    def display(self):
        """
        Gets a string representation of the corner using a similar character map from area.
        :return: a string representation of the corner
        """
        return get_symbol(self.neighbours)

    def __repr__(self):
        """
        Returns a string representation of the corner.
        """
        return self.display()

class Edge:
    """
    Represents the border in the intersection between edges of adjacent areas. Centres of areas are temporarily represented by this
    """
    def __init__(self, type, passable):
        """
        Type debotes whether the edge is vertical(1) or horizontal(0)
        Passable indicates whether the edge is a filled line or spaces
        """
        self.type = type
        self.passable = passable

    def display(self):
        """
        Returns a string representation of the edge based on its type and passability.
        :return: a string representation of the edge
        """
        if self.type == 0:
            if self.passable:
                return "     "
            else:
                return "─────"
        else:
            if self.passable:
                return " "
            else:
                return "│"

    def __repr__(self):
        """
        Returns a string representation of the corner.
        """
        return self.display()
