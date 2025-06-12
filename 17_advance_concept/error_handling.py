while True:
    try:

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("your sum of",a,"and",b,"is",f"{a/b}")
    except ValueError:
        print("Do not use")
    except ZeroDivisionError:
        print("Dont divide by 0")
    
    except:
        print("dd")
    