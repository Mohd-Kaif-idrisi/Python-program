# calling a function by function itself is called recursion,
# It is work like a loop and we have to call a function in the return in a function

def factorial(n):
    # in recursion if is called base recursion
    # it is very import to use base recursion to avoid infinite loop
    if n == 0 or n == 1:
        return 0
    else:
        return n * factorial(n-1)
    
print(factorial(5))    