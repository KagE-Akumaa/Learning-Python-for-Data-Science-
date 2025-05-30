l = [1, 3, 4, 5, 6]

a = [0] * len(l)
for i in range(len(l)):
    # print(i + 1)
    a[i] = l[i] ** 2
print(a)


b = []

for i in range(
    0, len(l), 2
):  # jump by two i = i + 2 similiar to for(int i = 0; i<l.size(); i = i+2)
    b.append(l[i])

print(b)

# for has an else too which will run after the for loop has completed its iterations

s = {"apple", 4.9, "cherry"}

for x in s:
    print(x)
else:
    print("Loop is completed")
print("Outside the loop")


# the else will not run if the for loop consits of any break statement as else is a part of for

i = 1
for x in s:
    print(x)
    i += 1
    if i == 2:
        break
else:
    print("Loop is completed")  # did not run cause of the break statement
print("Outside the loop")
