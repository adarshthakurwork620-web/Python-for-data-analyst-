''' Take age and print:
 - "Child" if age < 13 
 - "Teen" if age 13–19
 - "Adult" otherwise'''

age= int(input("Enter Age:"))
if age<13:
    print("Child")
elif age>=13 and age<18:
    print("Teen")    
else:
    print("Adult")