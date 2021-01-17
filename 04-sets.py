# Sets: unordered, mutable, no duplicates
myset = {1, 2, 3, 1, 2}
print(myset)

myset = set([1, 2, 3])
print(myset)

myset = set("Hello")
print(myset)

# Creating an empty set
myset = {}
print(type(myset)) # type is dict

myset = set()
print(type(myset)) # type is set

# Adding/Removing elements
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
myset.remove(1)
#myset.remove(4) # KeyError because '4' is not in set
myset.discard(4) # Ok
print(myset)

# Remove all with clear
myset.clear()
print(myset)

# Pop method, removes arbitrary value
myset = {1,2,3,4,5}
print(myset.pop())
print(myset.pop())
print(myset.pop())
print(myset.pop())

# Iterate through set with for-in-loop
myset = {1,2,3,4,5}
for i in myset:
  print(i, end=",")
print('')

# Check if element in set with if-in statement
if 1 in myset:
  print("yes")

# Unions
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
print(odds|evens)
print(odds.union(evens))
print(odds|primes)
print(evens|primes)

# Intersections
print(odds&evens)
print(odds.intersection(evens))
print(odds&primes)
print(evens&primes)

# Differences
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
print(setA - setB) # {4, 5, 6, 7, 8, 9}
print(setA.difference(setB))

# Symmetric Difference
print(setA.symmetric_difference(setB)) #{4, 5, 6, 7, 8, 10, 11, 12}

# Using Set update method. Modifies set in place
setA = {1, 2, 3}
setB = {4}
setA.update(setB)
print(setA) # {1, 2, 3, 4}

# Intersection upate method
setA = {1, 2, 3}
setB = {3, 4, 5}
setA.intersection_update(setB)
print(setA) # {3}

# Difference update method
setA = {1, 2, 3}
setB = {3, 4, 5}
setA.difference_update(setB)
print(setA) # {1, 2}

# Symmetric diffrence update
setA = {1, 2, 3}
setB = {3, 4, 5}
setA.symmetric_difference_update(setB)
print(setA) # {1, 2, 4, 5}