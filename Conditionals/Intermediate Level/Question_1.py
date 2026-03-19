'''Take three numbers and print the smallest.'''

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))

if a<b and a<c:
    print("smallest is A:",a)
elif b<c:
    print("smallest is B:",b)
else:
    print("smallest is C:",c)