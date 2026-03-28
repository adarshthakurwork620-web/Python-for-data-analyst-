'''
Given an integer N, print its multiplication table up to 10.
Input: 3
Output:
3 x 1 = 3
3 x 2 = 6
...
3 x 10 = 30
'''
n=int(input("Enter multiplication table :"))
multi=0
for i in range(1,11):
    multi=n*i
    print(f"{n}*{i}={multi}")