class Area:
  def findarea(self,a=None , b=None):
    if a!=None and b!=None:
      print("Area of Rectangle :",(a*b))
    elif a!=None :
      print("Area of square :",(a*a))
    else:
      print("nothing to find")
      
      
obj1=Area()
obj1.findarea()#is hai no parameter so it print noting to find
obj1.findarea(10)# it has one perameter then it give area of sqaure
obj1.findarea(10,20)# it has two perameter then it give area of rectangle 

# so all this has  same function but different parameter so this has functionoverloading  