''' Return value of given key from dictionary.
Input:
d= {"a":10,"b":20}
key="b"
Output:20
'''

d={}
n=int(input("Enter the size of key:value pairs:"))

for i in range(n):
    key=input("Enter the keys:")
    value=int(input("Enter the values:"))
    d[key]=value
print(d)
search_key = int(input("Enter key to search: "))

if search_key in d:
    print(d[search_key]) 
else:
    print("Key not found")    