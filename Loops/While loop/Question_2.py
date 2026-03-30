'''Reverse a number'''

a=input("Enter number:")

r=0
while a!=0:
    n=a%10
    r=r*10+n
    a=a//10
print("Reverse a number",r)    
# print(a[::-1])   