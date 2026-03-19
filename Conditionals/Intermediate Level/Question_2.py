''' Take number and print:
    - "Small" if < 10
    - "Medium" if 10–100
    - "Large" if > 100
'''
a=int(input("Enter a number:"))

if a<10:
    print("Small")
elif a>=10 and a<100:
    print("Medium")   
else:
    print("large")    