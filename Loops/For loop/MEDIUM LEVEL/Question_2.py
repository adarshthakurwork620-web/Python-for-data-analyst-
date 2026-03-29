'''Reverse digits of integer N.
Input: 123
Output:321
'''
a=int(input("Enter Number:"))
temp=a
count=0
r=0
#count the digits..
while temp>0:
    count+=1
    temp=temp//10
# loop is rum after the count of digits..
for i in range(count):
    n=a%10
    r=r*10+n
    a=a//10
print("Reverse=",r)    
