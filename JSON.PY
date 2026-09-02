import json

d={
  'course_name' : 'python',
   'feess':15000
}

f=json.dumps(d)
print(type(f))# it not distnory it is a JSON TYPE

print(f)