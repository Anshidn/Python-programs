class Shape:
    def draw(self):
        print("Drawing a shape")

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

triangle = Triangle()
circle = Circle()

triangle.draw()
circle.draw()