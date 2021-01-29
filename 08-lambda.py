# lambda arguments: expression
from functools import reduce

add10 = lambda x: x + 10
print(add10(5)) # 15

mult = lambda x,y: x * y
print(mult(2, 7)) # 14

def sort_by_y(x):
  return x[1]

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
points2D_sorted2 = sorted(points2D, key=lambda x: x[1])
points2D_sorted3 = sorted(points2D, key=sort_by_y)

print(points2D)
print(points2D_sorted)  # by x valus
print(points2D_sorted2) # by y values
print(points2D_sorted3) # by y values

# map function
print(list(map(lambda x: x*2, [1,2,3,4,5])))

# list comprehnsion syntax
print([x*2 for x in [1,2,3,4,5]])

# filter function
print(list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6])))

# list comprehension syntax
print([x for x in [1,2,3,4,5,6] if x % 2 == 0])

# reduce function
print(reduce(lambda acc, x: acc * x, [1,2,3,4,5,6], 1))

