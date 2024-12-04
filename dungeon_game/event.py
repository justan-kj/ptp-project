import random
class Event:
    def __init__(self, player):
        self.active = True
        self.player = player

    def activate(self):
        pass

class BlankEvent(Event):
    def __init__(self, player):
        super().__init__(player)

    def activate(self):
        print("Nothing eventful happens along the way.")

class TrapEvent(Event):
    def __init__(self,player):
        super().__init__(player)

    def activate(self):
        damage = random.randint(1,4)
        if self.active:
            self.active = False
            print(f"You walk into a trap and take {damage} damage!")
            self.player.modify_hp(-damage)
        else:
            print(f"You spot a previously encountered trap and carefully make your way around it.")

class RestEvent(Event):
    def __init__(self,player):
        super().__init__(player)
        self.description = "You stumble upon some leftover supplies."

    def activate(self):
        damage = random.randint(1,4)
        if self.active:
            self.active = False
            print(f"You discover some leftover supplies, using them to recover {damage} hp.")
            self.player.modify_hp(damage)
        else:
            print(f"You do not find any additional supplies along your path")

class PuzzleEvent(Event):
    def __init__(self,player):
        super().__init__(player)
        self.description = "You stumble upon a glowing tablet with a question inscribed upon it."

    def new_math_question(self):
        nums =  [random.randint(11,99),random.randint(11,99),random.randint(11,99)]
        question = f"What is {nums[0]} + {nums[1]} + {nums[2]}?"
        answer = str(int(sum(nums)))
        return question, answer

    def activate(self):
        if self.active:
            self.active=False
            damage = random.randint(2, 8)
            print(self.description)
            qn,ans = self.new_math_question()
            print(qn)
            if input("Answer: ") == ans:
                print("Congratulations, you have gotten the right answer!")
                print(f"You recover {damage} hp.")
                self.player.modify_hp(damage)
            else:
                print("You have given the wrong answer!")
                print(f"You take {damage} damage.")
                self.player.modify_hp(-damage)

        else:
            print("You pass by a dormant tablet.")







