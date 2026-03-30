'''Print all prime numbers between 1 and N.
Input: 10
Output:2 3 5 7
'''
n = int(input("Enter number: "))

for num in range(2, n + 1):
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")