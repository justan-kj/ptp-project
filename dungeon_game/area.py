from dungeon_game.direction import Direction

# WNES
char_map = {
    "0000": " ",
    "0001": "╷",
    "0010": "╶",
    "0011": "┌",
    "0100": "╵",
    "0101": "│",
    "0110": "└",
    "0111": "├",
    "1000": "╴",
    "1001": "┐",
    "1010": "─",
    "1011": "┬",
    "1100": "┘",
    "1101": "┤",
    "1110": "┴",
    "1111": "┼"
}


def get_symbol(exits):
    """
    Gets the symbol representing the exits for a room.
    A 4-char code is created where the 1st, 2nd, 3rd and 4th characters map to
    West, North, East and South exits respectively. 1 means the exit is active, 0 means it is inactive.

    Code is used as a key to a map of symbols, and the appropriate symbol is returned representing the state of room exits.

    :param exits: A dict of directions with their active state as boolean values
    :return: A 4 char code representing the state of the exits.
    """
    code = 0
    if exits[Direction.WEST]:
        code += 1000
    if exits[Direction.NORTH]:
        code += 100
    if exits[Direction.EAST]:
        code += 10
    if exits[Direction.SOUTH]:
        code += 1
    return  char_map[f"{code:>04}"]


class Area:
    """Represents a single space in the dungeon.

     Each Area records its position in the dungeon, any items held and the exits in 4 cardinal directions.
     """

    def __init__(self, position):
        """Initializes the area as a closed room (no exits)
        :param position: The Position of the area within the dungeon
        :return: None
        """
        self.exits = {
            Direction.NORTH: False,
            Direction.SOUTH: False,
            Direction.EAST: False,
            Direction.WEST: False
        }
        self.row = position.row
        self.col = position.col
        self.items = []

    def __repr__(self):
        """
        The str representation of the area depending on its exits.
        :return: A character from `char_map` showing the exits.
        """
        return  get_symbol(self.exits)
