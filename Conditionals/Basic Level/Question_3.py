'''
Take marks and print:
- "Fail" if < 35
- "Pass" if 35–59
- "First Class" if 60–79    
- "Distinction" if 80+
'''
marks= int(input("Enter Marks:"))
if marks<35:
    print("fail")
elif marks>=35 and marks<60:
    print("pass")
elif marks>=60 and marks<79:
    print("First class")        
else:
    print("Distinction")