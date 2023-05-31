mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict["email"] = "max@xyz.com"

print(mydict)

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["name"])
except KeyError:
    print("Error")

for value in mydict.values():
    print(value)

mydict_cpy = mydict
print(mydict_cpy)

