while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("enter second number: "))
        
        print("choose your opration:\n+ for sum\n- for subtract\n" \
            "* for multiply\n/ for divide\n** for square root\n% for remainder")
        
        o = input("Enter your opretor: ")
        
        match o:
            case '+':
                print(a,"+",b,"sum is = ",a+b)
            case '-':
                print(a,"-",b,"sum is = ",a-b)
            case '*':
                print(a,"*",b,"sum is = ",a*b)
            case '/':
                print(a,"/",b,"sum is = ",a/b)
            case '**':
                print(a,"**",b,"Exponentiation is = ",a**b)      
            case default:
                print("There was an error")
        q = input("Enter y to continue or n to exit: ")
        if q == "y":
            continue
        else:
            print("THANKS FOR USING")
            break
        
    except  ValueError:
        print("Enter a Valid value")
                   
                                           

