'''Reverse the order of words in a sentence.'''
s=input("Enter sentence:")
c="  ".join(s.split()[::-1])
print(c)