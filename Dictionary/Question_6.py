'''Return list of all keys.
 Return list of all values.
'''
d={}
n=int(input("size of dictionary:"))

for i in range(n):
    key=input("Enter keys:")
    value=int(input("Enter value:"))
    d[key]=value
print(d)
print("")
print("list of all keys:",list(d.keys()))
print("")
print("list of all values:",list(d.values()))    