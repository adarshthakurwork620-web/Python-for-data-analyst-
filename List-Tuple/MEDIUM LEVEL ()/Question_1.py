'''Return second largest element in list.'''

n=int(input("Enter the size of tuple:"))

list=[]
for i in range(1,n+1):
    num=int(input(f"Enter number {i} :"))
    list.append(num)
y=tuple((list))
print(y)


largest = 0
second=0
for num in range(len(y)):
    if tuple[i] > largest:
        second = largest
        largest = num
    elif tuple[i] > second and tuple[i] != largest:
        second = num

print(second)