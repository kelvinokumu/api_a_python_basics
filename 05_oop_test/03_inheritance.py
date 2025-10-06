class Animal:
    def speak(self):
        return "Make sound"


class Bird(Animal):
    def speak(self):
        return "Chirping"

parrot = Bird()
print(parrot.speak())