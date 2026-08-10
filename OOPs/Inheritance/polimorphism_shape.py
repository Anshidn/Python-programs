class Square:
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side * self.side
         

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
        

def show_area(shape):
    print(shape.area())

circle=Circle(3)
square=Square(5)

show_area(circle)
show_area(square)