"""
     2.Count vowels and consonants in a string.
"""

def CountVC(s):
     vowels_set = {'a','e','i','o','u'}
     vowels_c = consonant_c = 0

     for ch in s.lower(): #.lower() converts to lowercase
          if ch.isalpha(): # .isalpha check for alphabets
               if(ch in vowels_set):
                    vowels_c += 1
               else:
                    consonant_c += 1

     return vowels_c, consonant_c

s = input("Enter a string: ")

# tupple unpacking similar to destructuring in js
vowels, consonant = CountVC(s)

print("Vowels: ",vowels)
print("Consonants: ", consonant)