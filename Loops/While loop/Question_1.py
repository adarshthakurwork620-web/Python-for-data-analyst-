'''Count digits in a number'''

a=int(input("Enter number:"))
count=0
while a>0:
    count+=1
    a//=10
print("Count of digits in number=",count)    