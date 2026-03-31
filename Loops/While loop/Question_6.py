'''Count frequency of a digit in number'''
n=int(input("Enter number:"))
d=int(input("Enter the digit:"))
count=0
while n>0:
    if n%10==d:
        count+=1
    n//=10
print("Count frequency is:",count)
