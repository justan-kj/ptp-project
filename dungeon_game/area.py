

class Area:
    """The area class represents a single space the player move through. It has exits determining valid movement options"""
    def __init__(self):
        """Initializes the area. It is a closed room by default
        :return: None
        """
        self.exits = {
            'N':False,
            'E':False,
            'S':False,
            'W':False
        }
