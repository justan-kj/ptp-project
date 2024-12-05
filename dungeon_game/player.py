from dungeon_game.inventory import Inventory


class Player:
    """
    The Player class represents the entity controlled by the player. It stores the state of the player such as hp, position and name.
    """

    def __init__(self, starting_position, starting_hp=100):
        """
        Initialises the player.
        :param name: player name as a string
        :param starting_position: 2-tuple representing initial player coordinates within the map, in the form (rows,cols)
        :param starting_hp: integer representing hit points of the player. starts with full (current=max) hp
        """
        self.position = starting_position
        self.inventory = Inventory()


