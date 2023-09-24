print("Hello")
print("Machiavelli")
class NewAbility():
    def __init__(self, voice):
        self.voice = voice

    def scream(self):
        print(f"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA {self.voice}")

cat = NewAbility("meow")
cat.scream()