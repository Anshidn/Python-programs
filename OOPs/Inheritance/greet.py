class EnglishGreet:
    def greet(self):
        return "Hello"

class SpanishGreet:
    def greet(self):
        return "Hola"

def show_greet(greeting):
    print(greeting.greet())

english = EnglishGreet()
spanish = SpanishGreet()

show_greet(english)
show_greet(spanish)