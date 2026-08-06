#first method
w="Welcom  {} to {}  Wscubetech".format("hello",21)#is this is use defalt index strating from 0
print(w)
print()

w="Welcom  {0} to {1}  Wscubetech".format("hello",21)
print(w)#it give output according to given index if barket
w="Welcom  {1} to {0}  Wscubetech".format("hello",21)
print(w)
print()


w="Welcom  {a} to {b}  Wscubetech".format(a=21,b=10) #it use intailzation or use placeholder
print(w)


w="Welcom  {b:10} to {a}  Wscubetech".format(a=21,b=10) #in this b has 10 space or place but it can store only 2 because
#it hai 10 so left 8 space is empty print 
print(w)


w="Welcom  {b:^10} to {a}  Wscubetech".format(a=21,b=10) #^ it show that the 10 is start from mid space 
print(w)

w="Welcom  {b:>10} to {a}  Wscubetech".format(a=21,b=10) #>it show that the 10 is start from left space 
print(w)

w="Welcom  {b:<10} to {a}  Wscubetech".format(a=21,b=10) #< it show that the 10 is start from right space 
print(w)

w="Welcom  {b:<10} to {a:^10}  Wscubetech".format(a=21,b=10)
print(w)