course={
  'php': { 'duration':'2 months','fees':15000},
  'java': { 'duration':'2 months','fees':15000},
  'python': { 'duration':'2 months','fees':15000},
}

print(course)
print("")
print(course['php'])
print("")
print(course['php'] ['fees'])

print("")

for k,v in course.items():
  print(k,v)
  print("")
  
  print(k,v['duration'],v['fees'])  
  course['java']['fees']=2000