from abc import ABC,abstractmethod
class Device(ABC):
    @abstractmethod
    def boot(self):
        pass
class laptop(Device):

    def __load_os(self):
        print("loading operating system...")

    def __check_hardware(self):
        print("checking hardware...")

    def boot(self):

        self.__load_os()
        self.__check_hardware()

lap=laptop()
lap.boot()