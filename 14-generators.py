# generators are functions that return an object that can be iterated over
# - executes lazily. memory efficient.
# - instead of return. uses keyword 'yield'

def mygenerator():
  yield 3
  yield 2
  yield 1

# iterate over g with for-loop
g = mygenerator()
print(g)
for i in g:
  print(i)

# iterate using next(g)
g = mygenerator()
value = next(g)
print(value)
value = next(g)
print(value)
value = next(g)
print(value)
# value = next(g) # Raises StopIteration

# Can pass to functions that take iterables
g = mygenerator()
print(sum(g)) #6

# sorted
g = mygenerator()
print(sorted(g))

def countdown(num):
  print('Starting')
  while num > 0:
    yield num
    num -= 1 

g = countdown(4)
for i in g:
  print(i)