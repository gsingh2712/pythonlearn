
#type conversion
pi = 3.14
answer = 42
print(int(pi))
print(float(42))

#Strings
'Hello World' == "Hello Word" == """Hello World""" # all are same single/double/triple all quotes
print('Hello World' == "Hello World" == """Hello World""") # all are same single/double/triple all quotes

#multiline String in tripple quotes is used a comments
"""This is comment
not a String Value to assigned 
to a varibales
"""

#String Functions
"hello".capitalize() # capitalize 1st letter
print ("hello".capitalize()) # capitalize 1st letter

"hello".replace("e","a")
print("hello".replace("e","a"))

"hello".isalpha()
print("hello".isalpha())

"123".isdigit()
print("123".isdigit())

#Converting to List
print("some,csv,values".split(",") == ["some","csv","values"])

#Formatting
name="Gaurav"
machine="HAL"
st="Nice to meet you {0} I am {1}".format(name,machine)
print(st)

py3format=f"Nice to meet you {name} I am {machine}" #Only in python3
print(py3format)

#BOOLEAN
python_course=True
java_course=False
int(python_course) == 1
int(java_course) == 0
str(python_course) == "True"

# None is same as null
aliens_found = None