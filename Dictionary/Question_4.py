'''Return total number of keys in dictionary.'''

d={}
n=int(input("Enter the size of key:value pairs:"))

for i in range(n):
    key=input("Enter the keys:")
    value=int(input("Enter the values:"))
    d[key]=value
print(d)
print("total numbers of kyes:",len(d))