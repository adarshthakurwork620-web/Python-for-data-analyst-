'''Return sum of all dictionary values.'''

d={}
n=int(input("size of dictionary:"))

for i in range(n):
    key=input("Enter keys:")
    value=int(input("Enter value:"))
    d[key]=value
print(d)
print("sum of all dictionary values:",sum(d.values()))