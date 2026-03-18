'''Take a number and check if it is 1-digit, 2-digit, or 3-digit.'''

num=int(input("Enter number(0-999):"))

if num>=0 and num<=9:
    print("1-Digit")
elif num>=10 and num<=99:
    print("2-Digit")
elif num>=100 and num<=999:
    print("3-Digit")
else:
    print("wrong input")           
