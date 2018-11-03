students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id=332):
    student = {"name":name, "student_id":student_id}
    students.append(student)

def save_file(student,id):
    try:
        f = open("students.txt","a")
        f.write(student+","+id+"\n")
        f.close()
    except:
        print("Could not save the file")

def read_file():
    try:
        f = open("students.txt","r")
        for line in f.readlines():
            student_data = line.split(",")
            add_student(student_data[0],student_data[1])
        f.close()
    except:
        print("Could not read the file")



read_file()
print_students_titlecase()

#Raw input
addst=True
while addst:
    student_name = input("Enter Student name")
    student_id = input("Enter Student Id")
    add_student(student_name, student_id)
    save_file(student_name,student_id)
    add_st= input("Enter more Students [Y/N] ? ")
    #tertiary condition
    addst = True if add_st == "Y" else False

print_students_titlecase()


