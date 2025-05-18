

# THIS IS MY ALL ROUGH PRACTICE QUESION


# print("hello world")

# TYPECASTING
# a = "60"
# b = 60
# c = 60.00
# a1 = int(a)
# b1 = str(b)
# c1 = int(c)
# print(a1,type(a1))
# print(b1,type(b1))
# print(c1,type(c1))

# ARTHMETIC OPRETOR USING USER INPUT
# a = int(input("Enter your a: "))
# b = int(input("Enter your b: "))

# sum = a + b
# sub = a - b
# multi = a * b
# div = a / b

# print(a,"+",b,"=",sum)
# print(a,"-",b,"=",sub)
# print(a,"*",b,"=",multi)
# print(a,"/",b,"=",div)


# ASSIGNMENT OPRETOR
# a = 5
# a+=5
# print(a)


# WHICH ONE IS GREATER
# a = 10
# b = 5
# if a > b:
#     print("a is greater")

# 1 TO 10 NUMBER
# for i in range(1,11):
#     print(i)


# EVEN NUMBER FROM INPUT
# n = int(input("Enter your number: "))
# for i in range(1,n):
#     if(i%2 == 0):
#         print(i)


# FACTORIAL OF N NUMBER
# n = int(input("Enter your number "))
# for i in range (1,n):
#     n = n*i
# print(n)    


# BREAK CONDITION
# for i in range(1,10):
#     if i > 5:
#         break
#     print(i)

# SUM OF 1 TO 10
# sum = 0
# for i in range(1,11):
#     sum = sum+i
# print(sum)

# SQUARE OF NUMBER
# for i in range(1,11):
#     print(i*i)


# MULTIPLICTION TABLE FROM INPUT
# table = int(input("Enter your number "))
# for i in range(1,11):
#     print(table,"X",i,"=",table*i)


# LOWER AND UPPERCASE
# name = "My name is kaif"

# print(name.upper())
# name = "MY NAME IS KAIF"
# print(name.lower())


# FIND AND REPLACE
# name = "My name is kaif"
# print(name.find("is"))
# print(name.replace('is','kaif'))


# F-STRING
# name = 'john'
# age = 18
# print(f"my name is {name} and i am {age} years old")


# STRING SLICING AND LEN
# str = "My name is kaif"
# print(str[1:5])
# print(len(str))


# 1 TO N NUMBERS
# def toten(n):
#     for i in range(1,n+1):
#         print(i)

# print(toten(10))        


# SUM OF 2 NUMBERS
# def arth(a,b):
#     sum = a + b
#     return sum

# sum1 = arth(5,5)
# print(sum1)    


# CHECKING AVARAGE
# def avg(a,b,c):
#     avg = (a+b+c)/3
#     return avg

# avg1 = avg(2,2,2)
# print(avg1)


# CHECKING NUMBER IS DIVIDED FROM 5 TO 11
# def check(n):
#     if(n%5 == 0 and n%11 == 0):
#         print(n,"Number is divided")
#     else:
#         print("Not divided")
# check(1)       
# 


# PRINTING VOWEL OR CONSONENT
# def vowel(n):
#     if( n == 'a' or n == 'e' or n == 'i' or n == 'o' or n =='u'):
#         print(n," is Vowel")
#     else:
#         print(n," Is consoment")

# vowel('a')


# COUNTING VOWELS
# def co(n):
#     count = 0
#     for i in range(0,len(n)):
#         if n[i] == 'a' or n[i] == 'e' or n[i] == 'i' or n[i] == 'o' or n[i] =='u':
#             count = 1 + count 
#     print(count)
    
# co('kaif is a good boy')
    

# CHECKING AGE
# def check(age):
#     if age > 18:
#         print("You can drive")
#     elif age == 18:
#         print("Please apply for liceanse")
#     else:
#         print("you can not drive")        

# check(90)


# FACTORIAL OF N NUMBER
# def factorial(n):
#     for i in range(1,n):
#         n = n*i
#     return n
# ans = factorial(5)
# print(ans)    

# def greatest(a,b):


# FIND THE GREATER NUMBER
#     if a > b:
#         print(a," is Greater")
#     else:
#         print(b," is greater")

# print(greatest(5,4))


# MULTIPLICATION TABLE
# def table(n):
#     for i in range(1,11):
#         print(n*i)

# table(5)


# PRINT ODD EVEN NUMBERS
# def odd_even(n):
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             print(i)

# odd_even(10)


# FIND THE NUMBER IS POSITIVE, NEGATIVE OR ZERO
# def number(n):
#     if n > 0: 
#         print("Positive")
#     elif n == 0:
#         print("Zero")
#     else:
#         print("Negative")

# number(5)            


# SUM OF 1 TO N NUMBERS
# def sumofn(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum+=i

#     return sum

# ans = sumofn(10)
# print(ans)


# LAMBDA FUNCTION
# sum = lambda a,b: a+b
# print(sum(5,5))


# factorial by RECURSION

# def fact(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return n * fact(n-1)
    
# print(fact(5))


# Fibonacci by RECURSION

# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fib(n-2)+fib(n-1)
    
# print(fib(6))    


# PELINDROM BY function

# def pelindrom(n):
#     left = 0
#     right = len(n)-1

#     while left < right:
#         if n[left] != n[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# print(pelindrom("abcdcba"))

# RECURSION POWER FUNCTION
# def power(a,b):
    
#     if a == 0 or b == 0:
#         return 0
#     else:
#         return a**b
    
# print(power(2,3))    

# PELINDROM RECURSION


# def pelindrom(n):
#     if len(n) == 1:
#         return True
#     if n[0] != n[-1]:
#         return False
    
#     return pelindrom(n[1:-1])
    
# print(pelindrom("abcdcba"))    

# SUM OF DIGITS RECURSION

# def sum(n):
#     if n == 0 or n == 1:
#         return n
    
#     return n + sum(n-1)
    
# print(sum(5))    

list = [1,2,3,4,5]
list_2 = [6,7,8,9]
list.append(2)
print(list)

list.reverse()
print(list)

list.remove(3)
print(list)

list.pop()
print(list)

list.sort()
print(list)

list.insert(0,1)
print(list)

list.extend(list_2)
print(list)

table = [5*i for i in range(1,11)]
print(table)

table = []
for i in range(1,11):
    table.append(5*i)

print(table)    