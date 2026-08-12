class Students:
    def __init__(self):
        self.__marks = 100

    def get_private(self):
        return self.__marks

obj=Students()

print(obj.get_private())