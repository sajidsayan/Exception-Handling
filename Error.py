print("Plus")
try:
    a = int(input("Enter 1st num: "))
    b = int(input("Enter 2nd num: "))
    print("Result:",a+b)
except ValueError as error:
    print(error)
    
print("Minus")
try:
    a = int(input("Enter 1st num: "))
    b = int(input("Enter 2nd num: "))
    print("Result:",a-b)
except ValueError as error:
    print(error)
    
