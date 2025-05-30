"""
def addTwoNumbers(a, b):

    return a + b


a = 10
b = 15

print(addTwoNumbers(a, b))

"""
# handling order of arguments in function


def ReturnPrintArguments(a, b, c):
    print("a is", a)
    print("b is", b)
    print("c is", c)
    return a + 2, b, c + 1


def printArguments(a, b, c):
    print("a is", a)
    print("b is", b)
    print("c is", c)


first = 10
second = "game"
third = 9.8
printArguments(c=first, a=second, b=third)  # can change the order if parameters name are known

# Returning multiple values

# Similar to destructuring in js 
x, y, z = ReturnPrintArguments(first, second, third)

print(x, y, z)
