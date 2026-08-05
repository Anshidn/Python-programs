class Grandparent:
    def grandfather_feature(self):
        print("Grandfather: Expirience and wise ")
class father(Grandparent):
    def father_feature(self):
        print("Father : hardworking and caring")
class Aunt(Grandparent):
    def aunt_feature(self):
        print("Aunt : kind and supportive")
class Child(father,Aunt):
    def child_feature(self):
        print("Child :Energetic and curious")

c=Child()
c.grandfather_feature()
c.father_feature()
c.aunt_feature()
c.child_feature()