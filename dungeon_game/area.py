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
        code = get_symbol(self.exits)
        return char_map[code]


