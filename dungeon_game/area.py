from dungeon_game.direction import Direction


class Area:
    """The area class represents a single space the player move through. It has exits determining valid movement options"""
    def __init__(self,position):
        """Initializes the area. It is a closed room by default
        :return: None
        """
        self.exits = {
            Direction.NORTH: False,
            Direction.SOUTH:False,
            Direction.EAST:False,
            Direction.WEST:False
        }
        self.row = position.row
        self.col = position.col

    def __repr__(self):
        return f"R{self.row}C{self.col}"


