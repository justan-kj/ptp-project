class Choice:
    """
    The Choice class is a simple container containing a string as a text prompt and a value representing the outcome of the choice
    """
    def __init__(self, prompt,value):
        self.prompt = prompt
        self.value = value

    def __repr__(self):
        return self.prompt


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

    def get_choice(self, choices, is_first_move, selection=None):
        """
        Prints a list of choices sequentially and prompts a player to select one of them
        returning the Choice's value if the selection is succesful
        :param choices: The choices to be selected from
        :return: The value of the selected Choice
        """
        first_move_modifier = 0
        if is_first_move:
            first_move_modifier = 1
        if len(choices) + first_move_modifier == 1:
            flavor_text = f"The path leads to a dead end, you have no choice but to turn back."
        elif len(choices) + first_move_modifier == 2:
            flavor_text = f"The corridor continues straight towards the {choices[0].value}."
        elif len(choices) + first_move_modifier == 3:
            flavor_text = f"You reach a fork, with one path heading {choices[0].value}, and the other towards the {choices[1].value}"
        else:
            flavor_text = f"You arrive at a crossroads, the paths diverging in all directions."

        print(flavor_text)
        choice_num = 1
        for choice in choices:
            print(f"{choice_num}) {choice.prompt}")
            self.log.append(choice.prompt)
            choice_num+=1

        if not selection is None:
            self.log.append(choices[selection].prompt)
            return choices[selection].value

        while True:
            try:
                player_selection = int(input("Select a choice: "))
                if player_selection  <= len(choices):
                    self.log.append(choices[player_selection - 1].prompt)
                    return choices[player_selection-1].value
            except:
                print("Invalid choice")




