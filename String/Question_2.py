'''Count Substrings.
Input:s = "abc"
Output:6
'''
s=input("Enter words:")
l=len(s)
count=l*(l+1)//2
print("Substrings:",count)
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print(s[i:j])