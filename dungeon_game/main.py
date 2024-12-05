from dungeon_game.game import Game


def main():
    player_name = input("Welcome to Adventure world, please enter your character's name: ")
    new_game = Game()
    new_game.start()


if __name__ == '__main__':
    main()
