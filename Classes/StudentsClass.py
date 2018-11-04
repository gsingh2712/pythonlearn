students = []

class Student:

    school_name = "SpringField School" ## static attribute or Class attribute
    ## Class attributes will be same for all instances

    ##CONSTRUCTOR IN PYTHON
    ## self is must!!!
    def __init__(self, name, student_id=123):
        self.name = name
        self.student_id = student_id
        students.append(self)

    ## if you dont do this print(mark) will give memory location
    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

mark = Student("Mark",123)
print(mark)
jessica = Student("Jessica",123)
print(jessica)
james = Student("James",123)
print(james)

print(students)
