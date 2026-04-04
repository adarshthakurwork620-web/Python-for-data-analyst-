''' Return true if target exists in list.'''

n=int(input("Enter size of list:"))
list=[]
for i in range(1,n+1):
    num=int(input(f"Enter number {i} :"))
    list.append(num)
print("list:",list)    

target=int(input("Enter target number:"))

for i in range(n):
 if list[i]==target:
  print(True)