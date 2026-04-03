'''
Given a list of integers, return the sum of all elements.

'''
n = int(input("Enter number of elements: "))
list = []
for i in range(n):
    num = int(input("Enter number: "))
    list.append(num)   
total = sum(list)
print(total)    