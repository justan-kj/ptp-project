class Choice:
    """
    The Choice class is a simple container containing a string as a text prompt and a value representing the outcome of the choice
    """

    def __init__(self, prompt, value):
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

    def get_choice(self, choices, is_first_move):
        """
        Prints a list of choices sequentially and prompts a player to select one of them
        returning the Choice's value if the selection is succesful
        :param choices: The choices to be selected from
        :return: The value of the selected Choice
        """
        flavor_text = self.get_flavor_text(choices, is_first_move)
        print(flavor_text)
        self.display_choices(choices)
        return self.get_player_input(choices)

    def get_flavor_text(self, choices, is_first_move):
        first_move_modifier = 0
        if is_first_move:
            first_move_modifier = 1
        if len(choices) + first_move_modifier == 1:
            flavor_text = f"You have hit a dead end, there is no choice but to turn back."
        elif len(choices) + first_move_modifier == 2:
            flavor_text = f"The path continues towards the {choices[0].value}."
        elif len(choices) + first_move_modifier == 3:
            flavor_text = f"You reach a fork, with one path heading {choices[0].value}, and the other towards the {choices[1].value}"
        else:
            flavor_text = f"You arrive at a crossroads with paths diverging in all directions."
        return flavor_text

    def get_player_input(self, choices):
        while True:
            try:
                chosen_num = int(input("Select a choice: ")) - 1
                if 0 <= chosen_num < len(choices):
                    choice = choices[chosen_num]
                    self.log.append(choice.prompt)
                    return choice.value
                else:
                    print(f"Invalid choice, please select a number between 1 and {len(choices)}.")
            except ValueError:
                print("Invalid choice, please select a number.")

    def display_choices(self, choices):
        choice_num = 1
        for choice in choices:
            print(f"{choice_num}) {choice.prompt}")
            self.log.append(choice.prompt)
            choice_num += 1
