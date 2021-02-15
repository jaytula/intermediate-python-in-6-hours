import functools

# Two types of decorators
# - function decorators
# - class decorators

# Basic example of function decorator
def start_end_decorator(func):
  def wrapper():
    print("Start")
    func()
    print("End")
  return wrapper

@start_end_decorator
def print_name():
  print('Alex')

#print_name = start_end_decorator(print_name) # What actually happens when decorating
print_name()


def start_end_decorator_2(func):
  # Fixes issue with function identity
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print("Start2")
    result = func(*args, **kwargs)
    print("End2")
    return result
  return wrapper

@start_end_decorator_2
def add5(x):
  return x + 5

print(add5(7))

# Function identity
# Print out help. Note that Python is confused about name of function (i.e. 'wrapper')
#help(add5)
print(add5.__name__)

def repeat(num_times):
  def decorator_repeat(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(num_times):
        result = func(*args, *kwargs)
      return result
    return wrapper
  return decorator_repeat

@repeat(num_times=3)
def greet(name):
  print(f'Hello {name}')

greet('Alex')