import unittest

from dungeon_game.direction import Direction
from dungeon_game.game import GameContext
from dungeon_game.ui import UserInterface, Choice
from unittest.mock import patch


class TestUi(unittest.TestCase):
    def setUp(self):
        """Sets up a test ui
        :return: None
        """
        self.context = GameContext()
        self.ui = self.context.ui
        self.choices = [
            Choice("Head North", Direction.NORTH),
            Choice("Head South", Direction.SOUTH),
            Choice("Go Back", Direction.WEST)
        ]
        pass

    def test_init(self):
        """Checks that initialised values are as expected
        :return: None
        """
        self.assertEqual(self.ui.log, [])

    @patch('builtins.print')
    def test_update(self, mock_print):
        """Checks that messages are added to the log when update is called
        :return: None
        """
        self.ui.log = []
        self.ui.update("Test message 1")
        self.assertEqual(len(self.ui.log), 1)
        self.assertEqual(self.ui.log[0], "Test message 1")
        mock_print.assert_called_with("Test message 1")
        mock_print.reset_mock()
        self.ui.update("Test message 2")
        self.assertEqual(len(self.ui.log), 2)
        self.assertEqual(self.ui.log[1], "Test message 2")
        mock_print.assert_called_with("Test message 2")
        mock_print.reset_mock()

    def test_get_user_input(self):
        with patch('builtins.input', return_value=2):
            with patch('builtins.print') as mock_print:
                selected_value = self.ui.get_player_input(self.choices)
                self.assertEqual(selected_value, Direction.SOUTH)

    @patch('builtins.print')
    def test_display_choices(self, mock_print):
        self.ui.display_choices(self.choices)
        # Check if print was called correct number of times with correct arguments
        expected_calls = [
            unittest.mock.call("1) Head North"),
            unittest.mock.call("2) Head South"),
            unittest.mock.call("3) Go Back")
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)
