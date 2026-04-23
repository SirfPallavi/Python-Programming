# class Student:
#     def __init__ (self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade


# s1 = student()
# print(s1.name)
# print(s1.age)
# print(s1.grade)
  

#  class is a blueprint for creating objects.ANd object is a entity of class
class Student: 
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        # pass

s1 = Student("Alice", 20, "A")
print(s1.name,s1.age,s1.grade)

# s2 =Student()
# print(s2.name) 
