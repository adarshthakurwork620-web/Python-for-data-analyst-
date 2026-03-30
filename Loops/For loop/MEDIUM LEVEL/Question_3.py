'''Find largest digit in N.
Input: 5482
Output:8
'''
n = int(input("Enter number: "))
largest = 0
for  i in str(n):
    if int(i) > largest:
        largest = int(i)

print("Largest digit:", largest)
# print(max(a))
