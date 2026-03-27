'''Take username and check if username == "admin" or username == "root".'''

username=str(input("Enter username:"))

if username=="admin" or username=="root":
    print("Correct Username")
else:
    print("Username not Macth")