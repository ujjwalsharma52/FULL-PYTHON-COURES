import json

file = open("data.json", "r")

x = file.read()

finaldata = json.loads(x)

print(finaldata)

print()

for a in finaldata["courses"]:
    print(a)
    print()
    print(a["cname"], a["fees"])

file.close()