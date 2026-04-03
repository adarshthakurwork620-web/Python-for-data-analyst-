'''Count how many even numbers are present in the list.'''

n = int(input("Enter number of elements: "))

nums = []
for i in range(1,n+1):
    num = int(input(f"Enter number {i}:"))
    nums.append(num)
print(nums)    

count=0

for a in range(len(nums)):
    if nums[a]%2==0:
        count+=1
    else:
        count=0    
print("Even numbers are present in the list=",count)    