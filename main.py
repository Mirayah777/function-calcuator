def add(a,b):
    print("result is: ",a+b)

def sub(a,b):
    print("result is: ",a-b)

def division(a,b):
    if b == 0 :
        raise ZeroDivisionError
    print("result is: ",a/b)

def multiplication(a,b):
    print("result is: ",a*b)


print("choose an operatiom. 1-addition 2-subtration 3-division 4-multiplication")
choice = int(input("enter your choice: "))
if choice in (1,2,3,4):
    try:
        a = float(input("enter the first number: "))
        b = float(input("enter the second number: "))
        if choice == 1:
            add(a,b)
        elif choice == 2:
            sub(a,b)    
        elif choice == 3:
            division(a,b)   
        elif choice == 4:
            multiplication(a,b)   

    except ValueError:
        print("enter a valid no.")
    except ZeroDivisionError:
        print("division by 0 is not possible")
else:
    print(" invalid choice")
