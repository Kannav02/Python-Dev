# Functions are first-class objects , which mean they can be passed around and be used as an argument
def helloName(name):
    print(f"Hello {name}")
# the f here is a f string which is nothing but the same thing as interpolation in Javascript
def greetPerson():
    return helloName("Kannav")
# greetPerson()
# When a function is passed without the paranthese to aother function that means only a reference to the function is passed
# Decorator are functions which are used to extend the functionality of other functions


def checkString(func):
    def check2(name):
        if(type(name)!=str):
            return
        func(name)
    return check2
# @checkString is used to 
@checkString
def greet_Kannav(name):
    print(name)

greet_Kannav("Kannav")
