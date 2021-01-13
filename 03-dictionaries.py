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