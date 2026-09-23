class ws:
  def displayinfo(self):
    print("welcome to ws")
  
class IIP(ws):
  def displayinfo(self):
    super().displayinfo()# for this me can call tha prents class or do print hoga 
    print("welcome to IIP")
   
   
obj=IIP()
obj.displayinfo()# out welocme to IIP hoga class IIP ka function class ws ka function ko overwrite ka dega  

#is me do class hai or dono me same name ka function hai
# to class ws is prents class and class IIP is child class 
# is me child class me prents class ko inhertences kar diya 
# to child class ka function  prents class ka function ko overwrite kar dega
