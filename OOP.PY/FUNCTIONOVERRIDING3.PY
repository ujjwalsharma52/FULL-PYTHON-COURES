class A:
  def showdata(self):
    print("i m in A class ")
    
class B(A):
  def showdata(self):
    print("i m in B class")
    
    
obj=B()
obj.showdata()