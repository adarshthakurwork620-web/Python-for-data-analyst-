'''Print all factors of N.'''
n=int(input("Enter number:"))
if n<=0:
    print("Enter positive number:")
else:
    i=1
    while i<=n:
        if n%i==0:
            print(i,"",end="")
        i+=1    
     