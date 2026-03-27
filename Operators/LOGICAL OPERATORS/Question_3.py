'''Take number and check if not (number > 0).This is true when number is positive.
 This is false when number is 0 or negative.'''

number = int(input("Enter a number: "))

if not (number > 0):
    print("Number is zero or negative")
else:
    print("Number is positive")