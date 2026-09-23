class Student:
    __name = "ravi"

    def __init__(self):
        print(self.__name)
        self.__displayinfo()# YE SIRF CLASSS KI ANDER HI CALL HO SAKTA HAI

    def __displayinfo(self):
        print("welcome to wscubetech")


obj = Student()