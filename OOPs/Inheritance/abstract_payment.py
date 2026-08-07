from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class CardPayment(Payment):
    def pay(self):
        return "payment successful using Card!!"

class UPIPayment(Payment):
    def pay(self):
        return "payment successful using UPI!!"

c=CardPayment()
u=UPIPayment()
print(c.pay())
print(u.pay())