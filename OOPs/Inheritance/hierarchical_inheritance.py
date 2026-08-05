class vehicle:
    def start(self):
        print("Vehicle starting")
class car(vehicle):
    pass
class bike(vehicle):
    pass

c=car()
c.start()

c=bike()
c.start()