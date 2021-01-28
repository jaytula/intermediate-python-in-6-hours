# itertools: product, permutations, combinations, accumulate, groupby, and infinit iterators
# - types that can be used in a for-in loop

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

# product for Cartesion product
print(list(product([1, 2], ['a', 'b'])))  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
print(list(product([1, 2], ['a'])))  # [(1, 'a'), (2, 'a')]
print(list(product([1, 2], ['a'], repeat=2)))  # [(1, 'a', 1, 'a'), (1, 'a', 2, 'a'), (2, 'a', 1, 'a'), (2, 'a', 2, 'a')]

# permutations (and with length option) - all possible orderings
print(list(permutations([1, 2, 3]))) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(list(permutations([1, 2, 3], 2))) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations (length argument required)
print(list(combinations([1,2,3,4], 2))) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# combinations_with_replacement
print(list(combinations_with_replacement([1,2,3,4], 2))) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

# accumlate
print(list(accumulate([1,2,3,4]))) # [1, 3, 6, 10]

# accumlate with custom func
print(list(accumulate([1,2,3,4], func=operator.mul))) # [1, 2, 6, 24]
print(list(accumulate([1,2,5, 3,4], func=max))) # [1,2,5,5,5]

# groupby
def smaller_than_3(x):
  return x < 3

group_obj = groupby([1,2,3,4], key=smaller_than_3)
for key, value in group_obj:
  print (key, list(value))

group_obj = groupby([1,2,3,4], key=lambda x: x < 3)
for key, value in group_obj:
  print (key, list(value))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
group_obj = groupby(persons, key=lambda x: 'older than 25' if (x['age'] > 25) else '25 or younger')
for key, value in group_obj:
  print(key, list(value))

group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
  print(key, list(value))

# infinite iterator: count
for i in count(10):
  print(i)
  if i == 15:
    break

# infinite iterator: cycle
count = 0
for i in cycle([1, 2, 3]):
  if count > 15:
    break
  print(i)
  count += 1

# infinite iterator: repeat
# repeats a single value 'a' `10 times`
for i in repeat('a', 10):
  print(i)