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