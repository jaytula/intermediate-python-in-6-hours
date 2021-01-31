# Errors and Exceptions

try:
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

  x = -5
  assert (x > 0), 'x is not positive'
except:
  pass

try:
  a = 5 /0
except Exception as e:
  print(e)

try:
  g = 20
  a = 5 / 0
  b = 10 + '10'
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)
else:
  print('Everything okay')
finally: # always runs no matter if there is exception or not
  print('Cleaning up here')