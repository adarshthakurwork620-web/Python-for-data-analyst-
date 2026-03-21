''' 
    Take a number and print:
    - "Fizz" if divisible by 3
    - "Buzz" if divisible by 5
    - "FizzBuzz" if divisible by both
    - otherwise print number
'''
a=int(input("Enter a number:"))
if a%3==0 and a%5==0:
    print("FizzBuzz")
elif a%5==0:
    print("Buzz") 
elif a%3==0:
    print("Fizz")    
else:
    print(a)       
