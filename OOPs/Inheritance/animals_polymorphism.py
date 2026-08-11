class Dog:
    def speak(self):
        return "woof!"

class Cat:
    def speak(self):
        return "meow"

class Cow:
    def speak(self):
        return "Maaa"

animals=[Dog(),Cat(),Cow()]

for animal in animals:
    print(animal.speak())