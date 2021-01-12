# Tuples

# - Collection Type that is ordered and immutable
mytuple = ("Max", 28, "Boston")
print(mytuple)

# Parens are optional
mytuple2 = "Max", 28, "Boston"
print(mytuple2)

# One element tuple example, requires a comma
oneElemTuple = ("Max",)
print(type(oneElemTuple))

# tuples created from iterables
tupleExample = tuple(["Max", 28, "Boston"])
print(tupleExample)

# Access item by bracket indexing
item = tupleExample[0]
itemLast = tupleExample[-1]

# Iterate over tuple
for i in tupleExample:
  print(i)

# Check if item in tuple with `in`
if "Max" in tupleExample:
  print('yes')
else:
  print('no')

# Length of tuple
letters = ('a', 'p', 'p', 'l', 'e')
print(len(letters))

print(letters.count('p')) # 2
print(letters.index('p')) # 1

# List conversion
lettersList = list(letters)
print(lettersList)

# tuple conversion
print(tuple(lettersList))

# slicing
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers[2:5]) # 3, 4 ,5

# slicing with step
print(numbers[::2])

# reverse tuple trick with negative one step
print(numbers[::-1])

# Unpacking
person1 = "Max", 28, "Boston"
name, age, city = person1
print(name, age, city)

# Unpack with star
numbers = (0, 1, 2, 3, 4)
i1, *i2, i3 = numbers
print(i1) # 0
print(i2) # [1, 2, 3]
print(i3) # 4

import sys

# Tuples can be more size-efficient because they are immutable
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# It can be more efficient to iterate over a tuple
import timeit

print(timeit.timeit(stmt="[0, 1, 2, 3, 4,5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4,5)", number=1000000))