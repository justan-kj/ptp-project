class Choice:
    """
    The Choice class is a simple container containing a string as a text prompt and a value representing the outcome of the choice
    """
    def __init__(self, prompt,value):
        self.prompt = prompt
        self.value = value


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

    def get_choice(self, choices, selection=None):
        """
        Prints a list of choices sequentially and prompts a player to select one of them
        returning the Choice's value if the selection is succesful
        :param choices: The choices to be selected from
        :return: The value of the selected Choice
        """
        choice_num = 1
        for choice in choices:
            print(f"{choice_num}) {choice.prompt}")
            self.log.append(choice.prompt)
            choice_num+=1

        if not selection is None:
            self.log.append(choices[selection].prompt)
            return choices[selection].value
        while True:
            player_selection = input("Select a choice: ")
            try:
                if int(player_selection) - 1 in range(len(choices)):
                    self.log.append(choices[player_selection].prompt)
                    return choices[player_selection].value
            except:
                print("Invalid choice")




