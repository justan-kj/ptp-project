class UserInterface:
    def __init__(self):
        self.log = []

    def update(self, message):
        self.log.append(message)
        print(message)
        pass

