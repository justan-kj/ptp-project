from dungeon_game.direction import Direction

#WNES
char_map = {
    "0000":" ",
    "0001":"╷",
    "0010":"╶",
    "0011":"┌",
    "0100": "╵",
    "0101":"│",
    "0110":"└",
    "0111": "├",
    "1000":"╴",
    "1001":"┐",
    "1010":"─",
    "1011":"┬",
    "1100":"┘",
    "1101":"┤",
    "1110":"┴",
    "1111":"┼"
}

def get_symbol(exits):
    """
    Gets the symbol code exits for a room.
    The code is 4 characters with the 1st, 2nd, 3rd and 4th characters represent
    West, North, East and South exits respectively. 1 means the exit is active, 0 means it is inactive.

    :param exits: A dict of directions with their active state as boolean values
    :return: A 4 char code representing the state of the exits.
    """
    value = 0
    if exits[Direction.WEST]:
        value += 1000
    if exits[Direction.NORTH]:
        value += 100
    if exits[Direction.EAST]:
        value += 10
    if exits[Direction.SOUTH]:
        value += 1
    return f"{value:>04}"


class Area:
    """The area class represents a single space in the dungeon.

     Each Area records its position in the dungeon and the exits in 4 cardinal directions."""
    def __init__(self,position):
        """Initializes the area as a closed room.
        :param position: The Position of the area within the dungeon
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
        """
        Returns the str representation of the area depending on its exits.
        :return: A character from `char_map` showing the exits.
        """
        code = get_symbol(self.exits)
        return char_map[code]


