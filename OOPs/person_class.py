#class=blueprint
class person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello",self.name)
p1 = person("Anshid",18)
p2 = person("Jose",34)
p1.greet()
p2.greet()