import unittest
from dungeon_game.ui import UserInterface, Choice

class TestUi(unittest.TestCase):
    def setUp(self):
        """Sets up a test ui
        :return: None
        """
        self.ui = UserInterface()
        pass

    def testInit(self):
        """Checks that initialised values are as expected
        :return: None
        """
        self.assertEqual(self.ui.log, [])

    def testUpdate(self):
        """Checks that messages are added to the log when update is called
        :return: None
        """
        self.ui.log = []
        self.ui.update("Test message 1")
        self.assertEqual(len(self.ui.log), 1)
        self.assertEqual(self.ui.log[0], "Test message 1")
        self.ui.update("Test message 2")
        self.assertEqual(len(self.ui.log), 2)
        self.assertEqual(self.ui.log[1], "Test message 2")

    def testChoices(self):
        self.ui.log = []
        choices = [Choice("Test choice 1", "val2"),
                   Choice("Test choice 2", "val2"),
                   Choice("Test choice 3", "val2")]
        self.assertEqual(self.ui.get_choice(choices,1),"val2")
        self.assertEqual(self.ui.log[-1], "Test choice 2")