class Students:
    def __init__(self):
        self.__mark = 50

    def set_mark(self,mark):
        self.__mark = mark

    def get_mark(self):
        return self.__mark

student=Students()
print(student)
print(student.get_mark())