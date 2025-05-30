"""
     3. Replace all spaces in a string with dashes `-`.
"""

def Replace_S(s):

     temp_s = ""
     for ch in s:
          if(ch == " "):
               temp_s+= '_'
          else:
                temp_s+= ch

     return temp_s
     


s = input("Enter the string: ")

newS = Replace_S(s)

# or use built in function

temp_s = s.replace(" ", "_")

print(newS)
print(temp_s)