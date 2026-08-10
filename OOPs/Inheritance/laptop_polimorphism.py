class Laptop:
    def price(self,amount):
        return amount

class GamingLaptop(Laptop):
    def price(self):
        return 110000

class BussinessLaptop(Laptop):
    def price(self):
        return 100000

gaming = GamingLaptop()
bussiness = BussinessLaptop()

print(gaming.price())
print(bussiness.price())