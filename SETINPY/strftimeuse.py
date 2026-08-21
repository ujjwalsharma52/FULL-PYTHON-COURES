import datetime #IT GIVE CURRRNT TIME

x=datetime.datetime.now()
m=x.strftime("%Y")#ye century bhi dega and year bhi full
n=x.strftime("%y")#is ka output sirf 26 matlb only year dega century nahin dega
o=x.strftime("%b")#haif name of month name example aug not full name
p=x.strftime("%B")#it give full name of month name example august
q=x.strftime("%M")#it give minates
r=x.strftime("%m")#it give month in number
s=x.strftime("%S")#it give sec
t=x.strftime("%H")#it give time according to 24 means train type
u=x.strftime("%I")#it give time according to 12 means watch type
v=x.strftime("%p")#it give AM/PM


#print(x) 

print(m)
print(n)
print(o)
print(p)
print(q)
print(r)
print(s)
print(t)
print(u)
print(v)


#print(datetime.datetime(2024,7,19))