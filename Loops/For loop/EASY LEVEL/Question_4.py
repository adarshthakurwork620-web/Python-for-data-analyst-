'''Print squares of numbers from 1 to N.
Input: 4
Output:1 4 9 16
'''
n=int(input("Enter number:"))

square=0
for i in range(1,n+1):
    square=i**2

    print(square,"",end="")