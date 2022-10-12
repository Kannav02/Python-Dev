class Person:
    # class attribute
    attributeName="Kannav"
    # the self parameter is a reference to the current instance of the class
    # its the same as this in c++ and java
    # instance attributes
    # a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API
    #  (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change
    #  without notice.
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # _init_ is a special method which is called when an object is created from a class and is same as the constructor in other languages
    # instance method
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

class Student(Person):
    def __init__(self,studentID,name,age):
        self.studentID=studentID

        Person.__init__(self,name,age)
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old and my student ID is {self.studentID}")


Kannav=Student(1,"Kannav",19)
Kannav.say_hello()

