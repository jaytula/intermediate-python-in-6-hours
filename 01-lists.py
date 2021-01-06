# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "applee"]
print(mylist)

# Create an empty list with list()
mylist2 = list()
print(mylist2)

# Lists can contain different types
mylist3 = [5, True, "apple", "apple"]
print(mylist3)

# Access element by referring to index
print(mylist3[1])

# If index out of range, we get IndexError

# Get last itm with negative indexing
print(mylist[-1])

# Iterate with for-in loop
for i in mylist:
  print(i)