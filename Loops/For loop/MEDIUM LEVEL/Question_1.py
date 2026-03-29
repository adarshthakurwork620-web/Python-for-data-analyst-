'''Compute factorial of N using loop.
Input: 5
Output:120
'''
a=int(input("Enter Number:"))

if a<0:
    print("worng input")
elif a==0:
    print("factorial=1")
else:
    fact=1
    for i in range(1,a+1):
        fact*=i
    print(f"factorial of {a} = {fact}")