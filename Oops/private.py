class Person:
    __name = "john doe"
    # privae attribute 
    def __init__(self,name,age):
       self.name= name
       self.age=age

    def __hello(self):
           print("Hello person")
    def welcome(self):
                self.__hello()

p1 =Person("Alice",30)
print(p1.name,p1.age)
print(p1.welcome())
