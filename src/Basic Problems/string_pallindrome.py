"""
     1. Check if a string is a palindrome.
"""

def checkPallindrome(s):
     l = 0
     r = len(s)-1

     while(l <=r):
          if(s[l] != s[r]):
               return False
          l += 1
          r -= 1
     return True

s = input("Enter the string: ")

check = checkPallindrome(s)

if(check):
     print(s," is a pallindrome string")
else:
     print(s, " is not a pallindrome string")