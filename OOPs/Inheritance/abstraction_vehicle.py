from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(Vehicle):
    def start(self):
        return "Car started"

class bike(Vehicle):
    def start(self):
        return "Bike started"

c=car()
b=bike()
print(c.start())
print(b.start())