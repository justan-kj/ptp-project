

class Player():
    """
    The Player class represents the entity controlled by the player. It stores the state of the player such as hp, position and name.
    """
    def __init__(self, name, starting_position=(0,0), hp=100):
        """
        Initialises the player.
        """
        self.name = name
        self.position = starting_position
        self.max_hp = hp
        self.current_hp = hp


