try:
    x=int(input("enter first number"))
    y=int(input("enter second number"))
    print(x/y)
except ZeroDivisionError:
    print("cannot divide with zero")
except ValueError:
    print("give int values")    
print()        
try:
    x=int(input("enter first number"))
    y=int(input("enter second number"))
    print(x/y)
except (ZeroDivisionError,ValueError)as msg:
    print("provde valid input values only",msg)
    