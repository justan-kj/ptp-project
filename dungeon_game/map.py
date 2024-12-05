from dungeon_game.direction import Direction
from dungeon_game.area import get_symbol


class Map:
    def __init__(self, areas):
        self.areas = areas
        self.borders = self.build_borders()

    def build_borders(self):
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
        self.build_borders()
        for row in self.borders:
            line = ""
            for col in row:
                line += col.display()
            print(line)


class Corner:
    def __init__(self, row, col, max_row, max_col):
        self.neighbours = {
            Direction.NORTH: row > 0,
            Direction.SOUTH: row < max_row - 1,
            Direction.EAST: col < max_col - 1,
            Direction.WEST: col > 0,
        }

    def display(self):
        return get_symbol(self.neighbours)
    def __repr__(self):
        return self.display()

class Edge:
    def __init__(self, type, passable):
        self.type = type
        self.passable = passable

    def display(self):
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
        return self.display()
