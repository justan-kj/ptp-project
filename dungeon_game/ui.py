class UserInterface:
    """The UserInterface class stores and presents the text prompts the player
     interacts with"""
    def __init__(self):
        """Initializes the ui. Log contains all the messages that have been displayed thus far
        :return: None
        """
        self.log = []

    def update(self, message):
        """
        Prints a message to the console then saves it into the log
        :param message: The message to be displayed and saved
        :return:
        """
        self.log.append(message)
        print(message)
        pass

