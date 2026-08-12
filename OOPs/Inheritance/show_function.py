class Dog:
    def show(self):
        print("This is a dog")

class Cat:
    def show(self):
        print("This is a Cat")

def display(animal):
    animal.show()

dog=Dog()
cat=Cat()

display(dog)
display(cat)