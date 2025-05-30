"""
Function which supports any number of arguments passed to it basically a generic function
"""
"""
A tuple in Python is an ordered, immutable collection of elements.
| Property              | Description                                    |
| --------------------- | ---------------------------------------------- |
| **Ordered**           | Elements maintain their position (like a list) |
| **Immutable**         | Once created, elements cannot be changed       |
| **Allows Duplicates** | Yes                                            |
| **Indexed**           | Yes — you can access elements via index        |
| **Can hold any type** | Numbers, strings, lists, other tuples, etc.    |

"""
# args will create a tuple of every argument that is passed to it as its a tuple its immutable so we can't change the elements inside args like args[i] = 2 not allowed
def add(*args): 
     sum = 0
     for i in range(len(args)):
          sum += args[i]
     return sum


a = add(2,3,4,5)
print(a)

print(add(10,20,30))

"""
Similar to rest operator in js

function add(...args) {
  let sum = 0;
  for (let i of args) {
    sum += i;
  }
  return sum;
}

console.log(add(2, 3, 4, 5)); // 14
"""