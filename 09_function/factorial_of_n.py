def factorial(n):
    for i in range(1,n):
        n = n*i
    return n

fact = factorial(5)
print(fact)    