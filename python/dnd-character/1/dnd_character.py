import random
def modifier(value):
    return (value - 10) // 2

class Character:
    def __init__(self):
        self.strength = Character.initialize_stat()
        self.dexterity = Character.initialize_stat()
        self.constitution = Character.initialize_stat()
        self.intelligence = Character.initialize_stat()
        self.wisdom = Character.initialize_stat()
        self.charisma = Character.initialize_stat()
        self.hitpoints = 10 + modifier(self.constitution)


    @staticmethod
    def roll_d6():
        return random.choice(range(1, 7))

    @staticmethod
    def initialize_stat():
        rolls = [Character.roll_d6() for _ in range(4)]
        return sum(rolls) - min(rolls)

    def ability(self):
        return 3


