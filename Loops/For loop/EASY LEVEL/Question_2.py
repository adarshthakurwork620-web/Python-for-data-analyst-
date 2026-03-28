'''Sum of First N Numbers.
Input: 5
Output:15
'''
n=int(input("Enter Number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(f"Sum of First {n} Numbers{sum}")