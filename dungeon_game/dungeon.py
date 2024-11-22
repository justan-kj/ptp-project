from dungeon_game.area import Area

class Dungeon():
    """The Dungeon class represents the space the player passes through.
    It contains the areas a player can move through"""
    def __init__(self, size):
        """Initializes the dungeon.
        :param size: a 2-tuple of the form (rows, columns)
        :return: None
        """
        rows, cols = size
        self.areas = [[Area() for _ in range(cols)] for _ in range(rows)]






