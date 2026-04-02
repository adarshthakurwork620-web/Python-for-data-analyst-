'''Count uppercase and lowercase letters.'''
s=input("Enter string:")
upper=0
lower=0
for ch in s:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower += 1    
print("uppercase letters:",upper)
print("lowercase letters:",lower)