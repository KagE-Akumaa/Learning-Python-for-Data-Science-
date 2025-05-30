"""
Given a list of numbers eg.. [1,2,4,-5,7,9,3,2] make a new list in sorted ascending order
"""

og_l = [1, 2, 4, -5, 7, 9, 3, 2]

l = og_l[:]

sorted_ans = []

while l:
    min = 999999
    idx = -1
    for j in range(len(l)):
        if l[j] < min:
            min = l[j]
            idx = j
    sorted_ans.append(min)
    del l[idx]

print(sorted_ans)
