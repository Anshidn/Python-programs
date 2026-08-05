class Grandparent:
    def grandfather_feature(self):
        print("Grandfather feature")
class father(Grandparent):
    def father_feature(self):
        print("Father Feature")
class Child(father):
    def child_feature(self):
        print("Child feature")

c=Child()
c.grandfather_feature()
c.father_feature()
c.child_feature()