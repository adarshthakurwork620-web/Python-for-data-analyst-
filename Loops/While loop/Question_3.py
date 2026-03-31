'''Print Fibonacci series up to N terms'''
n = int(input("Enter number of terms: "))

a = 0
b = 1
count = 0

if n <= 0:
    print("Enter a positive number")
else:
    print(a,"",end="")
    while count < n:
        c = a + b
        a = b
        b = c
        count += 1
        print(a,"",end="")