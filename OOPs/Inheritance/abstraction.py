from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
     def sound(self):
          return "woof!!"

class cat(Animal):
     def sound(self):
         return "meow"

d = Dog()
c = cat()
print(d.sound())
print(c.sound())