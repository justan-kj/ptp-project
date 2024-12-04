
class Event:
    def __init__(self):
        self.active = True
        self.description = ""

    def activate(self):
        pass

class BlankEvent(Event):
    def __init__(self):
        super().__init__()
        self.description = "Nothing eventful happens along the way."

    def activate(self):
        return self.description


