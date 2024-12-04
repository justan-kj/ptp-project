import random
class Event:
    def __init__(self, player):
        self.active = True
        self.description = ""
        self.player = player

    def activate(self):
        pass

class BlankEvent(Event):
    def __init__(self, player):
        super().__init__(player)
        self.description = "Nothing eventful happens along the way."

    def activate(self):
        return self.description

class TrapEvent(Event):
    def __init__(self,player):
        super().__init__(player)
        self.description = "You walk into a trap!"

    def activate(self):
        damage = random.randint(1,4)
        self.player.modify_hp(-damage)
        return self.description + f"You took {damage} damage!"



