'''Create a dictionary with keys as names and values as ages. Return the dictionary.
Input:
names= ["Amit","Riya"]
ages= [25,30]
Output:{"Amit":25,"Riya":30}
'''
names= ["Amit","Riya"]
ages= [25,30]
y=dict(zip(names,ages))
print(y)
