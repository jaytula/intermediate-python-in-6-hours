import functools

# Two types of decorators
# - function decorators
# - class decorators

# Basic example of function decorator
def start_end_decorator(func):
  def wrapper(*args, **kwargs):
    print("Start")
    result = func(*args, **kwargs)
    print("End")
    return result
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

@repeat(3)
def greet(name):
  print(f'Hello {name}')

greet('Alex')

def debug(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    args_repr = [repr(a) for a in args]
    kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
    signature = ", ".join(args_repr + kwargs_repr)
    result = func(*args, **kwargs)
    print(f"{func.__name__!r} returned {result!r}")
    return result
  return wrapper

@debug
@start_end_decorator
def say_hello(name):
  greeting = f'Hello {name}'
  print(greeting)
  return greeting

say_hello('IU')

# class decorators - for maintaining and updating a state

class CountCalls:
  def __init__(self, func):
    self.func = func
    self.num_calls = 0

  def __call__(self, *args, **kwargs):
    self.num_calls += 1
    print(f'This is executed {self.num_calls} times')
    return self.func(*args, **kwargs)

@CountCalls
def say_hello():
  print('Hello')

say_hello()
say_hello()
say_hello()

# Typical Uses of decorators
# - Implement a timer decorator. Calculate executiontime of a function
# - Debug decorator. Print out information of the called function and its arguments
# - Check decorator. To check if args fulfill some requirement
# - Register functions. Like plugins
# - Cache return values
# - Add information or update state