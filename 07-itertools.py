# itertools: product, permutations, combinations, accumulate, groupby, and infinit iterators
# - types that can be used in a for-in loop

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate
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