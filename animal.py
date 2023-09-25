class Ability():
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello I am {self.name.title()}")

    def attack(self, dmg=7):
        print(f"{self.name.title()} attacked {dmg} dmg!")
        return dmg
