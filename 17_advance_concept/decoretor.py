def decoretor(func):
    def wrapper():
        print("Welcome")
        func()
        print("Thank you for using")
    return wrapper

@decoretor

def say_hello():
    print("hello")

say_hello()