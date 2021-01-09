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

# Check if item in list
if 'banana' in mylist:
  print('there is a banana')
else:
  print('theere is no banana')

# Determine number elements:
print(len(mylist))

# Append to list
mylist.append('lemon')
print(mylist)

# Insert item at specific position
mylist.insert(1, 'blueberry')
print(mylist)

# Remove last item
removed = mylist.pop()
print(removed, mylist)

# Remove specific element
mylist.remove('banana')
print(mylist)

# If we try to remove an item not in list we get a ValueError

# Remove all elements with clear
mylist.clear()
print(mylist)

# Reverse list. In-place
mylist = ["a", "b", "c", "e", "d"]
mylist.reverse()
print(mylist)

# Sort list with sort method. Sorts in place
mylist.sort()
print(mylist)

# Sort but do not modify original
mylist2 = ['z', 'y', 'x']
sorted2 = sorted(mylist2)
print(mylist2)
print(sorted2)

# Create a list with same element trick
mylist3 = [0] * 5
print(mylist3) # [0, 0, 0, 0, 0]

# Concat two list using '+'
mylist4 = [0, 1, 2, 3, 4, 5]
result_list = mylist3 + mylist4
print(result_list) # [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]

# Slicing
mylist5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mylist5[1:5])

# Step index
print(mylist5[::2]) # [1, 3, 5 ,7, 9]

# Copying lists (lists are reference types)
list_orig = ['banana', 'cherry', 'apple']
list_copy = list_orig # Same reference
list_orig.append('lemon')
print(list_orig)
print(list_copy)

# Copying the right way
list_copy2 = list_orig.copy()
list_copy3 = list(list_orig) # Another way to copy
list_copy4 = list_orig[:] # Slicing as a way to copy
list_orig.append('blueberry')
print(list_orig)
print(list_copy2)

# List comprehension - Expression and for-in loop over the list
list_of_nums = [1, 2, 3, 4, 5]
square_of_nums = [i*i for i in list_of_nums]
print(square_of_nums)