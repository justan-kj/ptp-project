from enum import Enum

class Direction(Enum):
    NORTH = [(-1,0),"North","N"]
    SOUTH = [(1,0), "South", "S"]
    EAST = [(0,1), "East", "E"]
    WEST = [(0,-1), "West", "W"]

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