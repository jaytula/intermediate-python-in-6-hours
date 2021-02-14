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