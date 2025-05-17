# print("hello world")

# a = "60"
# b = 60
# c = 60.00

# a1 = int(a)
# b1 = str(b)
# c1 = int(c)

# print(a1,type(a1))
# print(b1,type(b1))
# print(c1,type(c1))

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


# a = 5

# a+=5
# print(a)

# a = 10
# b = 5
# if a > b:
#     print("a is greater")

# for i in range(1,11):
#     print(i)

# n = int(input("Enter your number: "))
# for i in range(1,n):
#     if(i%2 == 0):
#         print(i)

# n = int(input("Enter your number "))
# for i in range (1,n):
#     n = n*i
# print(n)    

# for i in range(1,10):
#     if i > 5:
#         break
#     print(i)

# sum = 0
# for i in range(1,11):
#     sum = sum+i
# print(sum)

# for i in range(1,11):
#     print(i*i)

# table = int(input("Enter your number "))
# for i in range(1,11):
#     print(table,"X",i,"=",table*i)

# name = "My name is kaif"

# print(name.upper())

# name = "MY NAME IS KAIF"

# print(name.lower())

# name = "My name is kaif"

# print(name.find("is"))
# print(name.replace('is','kaif'))

# name = 'john'
# age = 18

# print(f"my name is {name} and i am {age} years old")

# str = "My name is kaif"

# print(str[1:5])
# print(len(str))

# def toten(n):
#     for i in range(1,n+1):
#         print(i)

# print(toten(10))        

# def arth(a,b):
#     sum = a + b
#     return sum

# sum1 = arth(5,5)
# print(sum1)    
    
# def avg(a,b,c):
#     avg = (a+b+c)/3
#     return avg

# avg1 = avg(2,2,2)
# print(avg1)

# def check(n):
#     if(n%5 == 0 and n%11 == 0):
#         print(n,"Number is divided")
#     else:
#         print("Not divided")
# check(1)       
# 

# def vowel(n):
#     if( n == 'a' or n == 'e' or n == 'i' or n == 'o' or n =='u'):
#         print(n," is Vowel")
#     else:
#         print(n," Is consoment")

# vowel('a')

# def co(n):
#     count = 0
#     for i in range(0,len(n)):
#         if n[i] == 'a' or n[i] == 'e' or n[i] == 'i' or n[i] == 'o' or n[i] =='u':
#             count = 1 + count 
#     print(count)
    
# co('kaif is a good boy')
    
# def check(age):
#     if age > 18:
#         print("You can drive")
#     elif age == 18:
#         print("Please apply for liceanse")
#     else:
#         print("you can not drive")        

# check(90)

# def factorial(n):
#     for i in range(1,n):
#         n = n*i
#     return n
# ans = factorial(5)
# print(ans)    

# def greatest(a,b):

#     if a > b:
#         print(a," is Greater")
#     else:
#         print(b," is greater")

# print(greatest(5,4))

# def table(n):
#     for i in range(1,11):
#         print(n*i)

# table(5)

# def odd_even(n):
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             print(i)

# odd_even(10)

# def number(n):
#     if n > 0: 
#         print("Positive")
#     elif n == 0:
#         print("Zero")
#     else:
#         print("Negative")

# number(5)            

def sumofn(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i

    return sum

ans = sumofn(10)
print(ans)