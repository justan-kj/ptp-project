from dungeon_game.inventory import Inventory


class Player:
    """
    The Player class represents the entity controlled by the player. It stores the state of the player such as position and name.
    """

    def __init__(self, starting_position):
        """
        Initialises the player.
        :param starting_position: 2-tuple representing initial player coordinates within the map, in the form (rows,cols)
        """
        self.position = starting_position
        self.inventory = Inventory()


