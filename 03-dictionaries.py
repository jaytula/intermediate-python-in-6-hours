mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

# Look-up key
value = mydict["name"]
print(value)
value = mydict["name"]
print(value)

# Update or add key
mydict["email"] = "max@xyz.com"
print(mydict)

# Delete a key
del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

# Remove last inserted key
mydict.popitem()
print(mydict)

# Check if key in dictionary and print out
if "city" in mydict:
  print(mydict["city"])

# Or use Try except
try:
  print(mydict["city"])
except KeyError:
  print("Error")

# Loop through dictionary
mydict3 = dict(name="Lucas", age=28, city="Phoenix")
for key in mydict3:
  print(key, end=",")
print("")

for key in mydict3.keys():
  print(key, end=",")
print("")

# Loop over values
for value in mydict3.values():
  print(value, end=",")
print("")

# Loop with both key and value available
for key, value in mydict3.items():
  print(key, value, end='|')
print('')

# Dictionaries are reference type. Be careful
mydict3_cpy = mydict3
mydict3_cpy["email"] = "max@xyz.com"

print(mydict3_cpy)  
print(mydict3)      # Also has email key

# To do a true copy, use builtin copy method
mydict3_real_copy = mydict3.copy()

# Another way to copy is with dict
mydict3_real_copy = dict(mydict3)

# Merge two dictionaries with update
mydict = dict(name="Max", age=28, email="max@xyz.com")
mydict_2 = dict(name="Mary", age=27, city="boston")
mydict.update(mydict_2)
print(mydict)

# Numbers can be keys
my_dict = {3: 9, 6: 36, 9: 81}

# Tuples can be keys
mytuple = (8, 7)
mydict = {mytuple: 15}
print(mydict)

# Note... A list cannot be a key
# type must be hashable to be a key