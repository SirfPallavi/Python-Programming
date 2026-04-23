class Student:
    college_name ="ABC College"
    name = 'anonymous'  
    # It is a class attriute which is shared by all the objects of the class.


    def __init__(self,name,marks):

        self.name = name
        # it is a oject attribute which is unique for each object of the class.
        # object attribute > Class attribute
        self.marks = marks
        print("adding new student in databases")

s = Student("Alice", 85)
print(s.name, s.marks)
print(Student.college_name)