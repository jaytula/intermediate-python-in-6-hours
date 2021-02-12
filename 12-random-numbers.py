import random

# Random float from 0 to 1
a = random.random()
print(a)

# random.uniform for float from start to end [0, 20]
print(random.uniform(0, 20))

# random integer using random.randint [0, 10]
print(random.randint(0, 10))

# random.randrange. does not include endpoint [0, 3)
print(random.randrange(0,3))

# random.normalvariate. picks a random value from a normal distribution
print(random.normalvariate(0, 1))

# pick random element from list
mylist = list("ABCDEFGH")
print(mylist)
print(random.choice(mylist))

# pick multiple elements (no dpulicates)
print(random.sample(mylist, 3))

# pick multiple elements allowing duplicates
print(random.choices(mylist, k=3))

# shuffle a list
print(random.shuffle(mylist))

# Ranbdom seeding to demonstrate psuedo-randomness
random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))

# Use secrets module for true randomness. Only has three functions
import secrets

print(secrets.randbelow(10)) # From [0, 10)
print(secrets.randbits(4)) # from [0, 15]
print(secrets.choice(list("ABCDEFGH"))) # Picks one at random

import numpy

# numpy.random.rand(number) returns array of floats betwen [0, 1)
print(numpy.random.rand(20))

# numpy.random.rand supports multi-dimensional arrays. for 3x3
print(numpy.random.rand(3, 3))

# Use randint for integers. 3 random integers
print(numpy.random.randint(0, 10, 3))

# use tuple with randint for multi-dimensional array
print(numpy.random.randint(0, 10, (3, 4)))

# Shuffles elements in the first axis
arr = numpy.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
numpy.random.shuffle(arr)
print(arr)

# Seed function for numpy
numpy.random.seed(1)
print(numpy.random.rand(3, 3))
print(numpy.random.rand(3, 3))
numpy.random.seed(1)
print(numpy.random.rand(3, 3))