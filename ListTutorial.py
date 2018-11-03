students = []

student_names = ["Mark","Katrina","Jessica"]

print(student_names[-1]) #last element

#adding elements at end
student_names.append("Homer")

print(student_names)

#contains check in list

if "Mark" in student_names:
    print("True")
else:
    print("False")

# Deleting an element "Jessica"
del student_names[2]
print(student_names)

## LIST SLICING -> Skipping a range of continuos cells

print(student_names[1:])

# For loops in list (easy way)

for name in student_names:
    print("Student name is {0}".format(name))


#range function in python gives you a list
