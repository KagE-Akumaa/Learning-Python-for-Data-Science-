"""
1. Find the max and min in a list.
"""


l = [1,2,6,3,7,0]

l_min = 99999
l_max = -99999

for i in range(len(l)):
     if(l[i] < l_min):
          l_min = l[i]
     if(l[i] > l_max):
          l_max = l[i]

print("minimum: ", l_min)
print("maximum: ", l_max)