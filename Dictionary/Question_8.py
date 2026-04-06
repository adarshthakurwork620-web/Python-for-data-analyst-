''' Remove a key from dictionary.'''

d={}
n=int(input("size of dictionary:"))

for i in range(n):
    key=input("Enter keys:")
    value=int(input("Enter value:"))
    d[key]=value
print(d)

remove_key=input("Enter the removing key:")

if remove_key in d:
    del d[remove_key]
    print("Updated dictionary:", d)
else:
    print("Key not found")    