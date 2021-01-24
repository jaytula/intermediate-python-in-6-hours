# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict

a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter) # Counter({'a': 5', 'b': 4', 'c': 3'})
print(my_counter.items()) # dict_items([('a', 5), ('b', 4), ('c', 3)])
print(my_counter.keys()) # dict_keys(['a', 'b', 'c'])
print(my_counter.values()) # dict_values([5, 4, 3])
print(my_counter.most_common(2)) # [('a', 5), ('b', 4)]
print(my_counter.elements()) # returns an iterable object: <itertools.chain object at 0x7efbfdfc4940>
print(list(my_counter.elements())) # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

# defaultdict: for undefined key, returns default value of type specified
d = defaultdict(float)
d['a'] = 1
d['b'] = 2
print(d)
print(d['a'], d['b'], d['c'])