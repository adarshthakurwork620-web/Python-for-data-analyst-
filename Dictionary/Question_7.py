''' Update value of a given key.'''

d = {}

n = int(input("Enter number of key-value pairs: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value
print(d)
update_key = input("Enter key to update: ")

if update_key in d:
    new_value = int(input("Enter new value: "))
    d[update_key] = new_value
    print("Updated dictionary:", d)
else:
    print("Key not found")