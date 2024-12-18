from dungeon_game.map import Map

class Choice:
    """
    The Choice class is a simple container containing a string as a text prompt and a value representing the outcome of the choice
    """
    def __init__(self, prompt, value):
        self.prompt = prompt
        self.value = value

class UserInterface:
    """The UserInterface class stores and presents the text prompts the player
     interacts with"""

    def __init__(self,context):
        """Initializes the ui. Log contains all the messages that have been displayed thus far
        :return: None
        """
        self.log = []
        self.context = context

    def update(self, message):
        """
        Prints a message to the console then saves it into the log
        :param message: The message to be displayed and saved
        :return:
        """
        self.log.append(message)
        print(message)

    def show_minimap(self):
        """
        Prints a string outline of the current area the player is in to aid navigation
        :return: None
        """
        player_pos = self.context.player.position
        area = self.context.dungeon.get_area(player_pos)
        Map([[area]]).display()

    def show_full_map(self):
        """
        Prints a string outline of all areas
        :return: None
        """
        Map(self.context.dungeon.areas).display()

    def prompt_player_movement(self, choices, moves):
        """
        Prints a list of choices sequentially and prompts a player to select one of them
        returning the Choice's value if the selection is succesful
        :param choices: The choices to be selected from
        :return: The value of the selected Choice
        """
        self.show_minimap()
        #
        flavor_text = self.get_flavor_text(choices, moves)
        print(flavor_text)
        self.display_choices(choices)
        chosen_direction = self.get_player_input(choices)
        self.update(f"You move towards the {chosen_direction.name}")
        return chosen_direction


    def get_movement_choices(self, moves, open_paths):
        """
        Generates choices for the player to take corresponding to all available exits for the room the player is in.
        Uses previous moves to asssign the last move as the "go back" option for easier navigating
        :param moves: The previous moves made by the player
        :param open_paths: A dict of directions representing the exits and their open/closed (true/false) state
        :return: the generated array of Choice objects
        """
        choices = []
        back_direction = None
        for key in open_paths:
            if len(moves) and key == moves[-1].opposite:
                back_direction = key
                continue
            if open_paths[key]:
                prompt = f"Move {key.name}"
                choices.append(Choice(prompt, key))
        if back_direction:
            choices.append(Choice(f"Go back ({back_direction.name})", back_direction))
        return choices


    def get_flavor_text(self, choices, moves):
        """
        Generates flavor text for the room exit layout based ont he number of choices (exits).
        :param moves: The previous moves made by the player
        :param choices: the array of choices available tot he player
        :return: the appropriate flavor text
        """
        first_move_modifier = 1
        if len(moves):
            first_move_modifier = 0
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
        """
        Attempts to get player input from the player until the player inputs a valid number corresponding to the index of a choice.
        Also allows player to view the map.
        :param choices: The array of choices available to the player
        :return: the value of the selected choice, expecting a Direction
        """
        while True:
            try:
                chosen_num = int(input("Select a choice: ")) - 1

                if 0 <= chosen_num <= len(choices):
                    if chosen_num == len(choices):
                        self.show_full_map()

                        continue
                    choice = choices[chosen_num]
                    self.log.append(choice.prompt)
                    return choice.value
                else:
                    print(f"Invalid choice, please select a number between 1 and {len(choices)}.")
            except ValueError:
                print("Invalid choice, please select a number.")

    def display_choices(self, choices):
        """
        Displays an array of choices ina  sequential manner
        :param choices: The array of choices available to the player1
        :return: None
        """
        choice_num = 1
        for choice in choices:
            print(f"{choice_num}) {choice.prompt}")
            self.log.append(choice.prompt)
            choice_num += 1
        print(f"{choice_num}) {"View Map"}")