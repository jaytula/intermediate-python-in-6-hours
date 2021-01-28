# lambda arguments: expression

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

