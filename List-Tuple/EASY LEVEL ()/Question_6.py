'''Return length of tuple'''

n=int(input("Enter the size of list:"))

list=[]
for i in range(1,n+1):
    num=int(input(f"Enter number {i} :"))
    list.append(num)
print(list)    
print("")
y=tuple((list))
print(y)
print("")
print("length of tuple:",len(y))
