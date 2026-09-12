#multpli lavle inheritance 
class A:
    def displayA(self):
        print("Ujjwal sharma A")


class B(A):#a is inheritance in b and funcation is creteed
    def displayB(self):
        print("raushan B")
        
class C(B):
    def displayC(self):
        print("shubhaam C")




# Object creation
#obj = B()
obj=C()

obj.displayA()
obj.displayB()
obj.displayC()