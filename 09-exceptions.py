# Errors and Exceptions
a = 5 + '10' # TypeError

import nonexistentmodule # Raised 'ModuleNotFoundError'

b = c # 'NameError' because 'c' is not defined

f = open('somefile.txt') # 'FileNotFoundError'

a = [1,2,3]
a.remove(4) # Raises ValueError
a[4] # IndexError

my_dict = {'name': 'Max'}
my_dict['age'] # KeyError

x = -5
if x < 0:
  raise Exception('x should be positive')