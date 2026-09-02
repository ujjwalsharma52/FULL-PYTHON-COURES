import json

d = '{"cname":"python","fees":1200,"duration":"2 months"}'

x = json.loads(d)

print(x)

print(type(x))

for a in x:
  print(a)#to get key 
  print(a,x[a])#for grting values