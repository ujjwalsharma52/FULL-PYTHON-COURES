class student :
  def __int__(self):
    self.__name=""
  def getname(self):#getname use 
    return self.__name
  def setname(self,name):#setname use 
    self.__name=name
    
obj=student()
obj.setname("Testing")
name=obj.getname()
print(name)