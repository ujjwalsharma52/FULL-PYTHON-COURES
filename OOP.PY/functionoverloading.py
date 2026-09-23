class WS:
  def displayinfo(self, name=''):
   print("welcome to wscubetech " +name)
  
obj=WS()
obj.displayinfo()# is me parameter nahi diya to sirf  welocm to 
#wscubetech print hoga name ka value print nahi hoga 
obj.displayinfo('Python') # is me welcometo wscubetech ki sath name ka value Python bhi print hoga 
#isko hi function overloading kahate hai same function per parameter change hai 
#same function different resulit de raha hai  