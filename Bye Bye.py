while True:
    y = int(input("Enter a year: "))
    if y % 400 == 0:
        print(y,"Its a leap year.")
    elif y % 100 == 0:
        print(y,"Its a not leap year.")
    elif y % 4 == 0:
        print(y,"Its a leap year.")
    else:
        print(y,"Its a not leap year.")
