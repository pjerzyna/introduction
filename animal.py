from random import randint
class Ability():
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello I am {self.name.title()}")

    def attact(self):
        dmg = randint(0,10)
        print(f"{self.name.title()} attacked {dmg} dmg!")

cat = Ability("Brajan")
cat.introduce()
cat.attact()