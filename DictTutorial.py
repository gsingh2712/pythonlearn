#key:values
student = {
    "name":"Mark",
    "id":123,
    "feedback": None
}

print(student["name"])
## OR
print(student.get("name"))

#extract all keys
keys = student.keys() # returns a list
print(keys)

for k in keys:
    print(k)

vals = student.values() # returns a list
print(vals)

# deleting a specific key
del student["name"]

print(student)
#List of Dictionaries
all_students = [
    {"name":"Mark","id":123},
    {"name":"Katrina","id":125},
    {"name":"Jessica","id":127}
]

