'''Take two numbers and swap them using arithmetic operators'''

a=int(input("1st number:"))
b=int(input("2nd number:"))
print(f"before swaping 1st number:{a} and 2nd number:{b}")
a=a+b
b=a-b
a=a-b

print(f"Affer swaping 1st number:{a} and 2nd number: {b}")