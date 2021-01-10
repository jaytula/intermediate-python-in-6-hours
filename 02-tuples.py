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