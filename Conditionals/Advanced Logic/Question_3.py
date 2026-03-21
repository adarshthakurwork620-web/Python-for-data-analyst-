'''Take two numbers and check if they are both even, both odd, or mixed.'''

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))

if a%2==0 and b%2==0:
    print("both even")
elif a%2!=0 and b%2!=0:
    print("both odd")   
else:
    print("mixed number")    