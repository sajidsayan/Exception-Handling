print("Divide")
try:
    a = int(input("Enter 1st num: "))
    b = int(input("Enter 2nd num: "))
    print("Result:",a/b)
except ZeroDivisionError as error:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter numerical number")
except:
    print("Runtime Error")
