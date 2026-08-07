from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay (self,amount):
        pass

class upi(payment):
    def pay(self,amount):
        print("paid",amount,"using upi")
class card(payment):
    def pay(self,amount):
         print("paid",amount,"using card")

p1=upi()
c1=card()
p1.pay(22222)
c1.pay(433443)