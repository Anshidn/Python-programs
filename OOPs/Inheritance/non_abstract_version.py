class Device:

    def __check_hardware(self):
        print("hardware checking...")


    def __load_os(self):
        print("operating system loading...")


    def boot(self):
        self.__check_hardware()
        self.__load_os()
        print("device is ready to use...")


device = Device()
device.boot()