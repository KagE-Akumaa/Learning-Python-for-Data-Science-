"""
Linear and binary search on a list
l = [1,2,4,6,7,8,9,20]
find:
1. if k exists eg.. k = 8
2. the index of k
"""
def binarySearch(l, k):
     r = len(l)-1
     left = 0
     while(left <= r):
          mid = (left+r)//2
          if(l[mid] == k):
               return mid
          elif(l[mid] > k):
               r = mid -1
          else:
               left = mid + 1
     return -1


def linearSearch(l, k):
    
     for i in range(len(l)):
          if(l[i] == k):
               return i
     
     return -1
l =  [1,2,4,6,7,8,9,20]
k = 8
a = linearSearch(l, k)
b = binarySearch(l,k)

print(k," is present on index: ", a)
print(k," is present on index: ", b)
