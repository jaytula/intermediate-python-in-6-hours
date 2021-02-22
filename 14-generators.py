import sys

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

# takes a log of memory
def firstn(n):
  nums = []
  num = 0
  while num < n:
    nums.append(num)
    num += 1
  return nums

print(firstn(10))
print(sys.getsizeof(firstn(1000000))) # 8697464 bytes

# firstn as generator: memory efficient
def firstn_generator(n):
  n = 0
  while n < 10:
    yield n
    n += 1

print(list(firstn_generator(10)))
print(sum(firstn_generator(10)))
print(sys.getsizeof(firstn_generator(1000000))) # 88 bytes

# fibonacci

def fib_generator(limit):
  curr, next = 0, 1
  while curr < limit:
    yield curr
    curr, next = next, curr+next

fib = fib_generator(200)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(list(fib))