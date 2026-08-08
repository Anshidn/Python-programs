radius=5
pi=3.14
class shape:
    def area(self):
        return 0

class Circle(shape):
    def area(self):
        return pi*radius*radius

class Triangle(shape):
    def area(self):
        return 10 * radius

shapes=[Circle(),Triangle()]
for s in shapes:
    print(s.area())