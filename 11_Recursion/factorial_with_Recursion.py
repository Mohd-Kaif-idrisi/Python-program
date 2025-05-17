# calling a function by function itself is called recursion,
# It is work like a loop and we have to call a function in the return in a function

def factorial(n):
    if(n == 0 or n == 1):
        return n
    else:
        return n * factorial(n-1)
    

print(factorial(5))    