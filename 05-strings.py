from timeit import default_timer as timer
# Strings are immutable
my_string = "Hello"
my_string = 'Hello'
print(my_string)

# Triple quotes for multi-line strings
my_string = """Hello
World"""
print(my_string)

# Backslash to suppress new line
print("""Hello\
 World""")

# Get character by index
my_string = "hello world"
print(my_string[1]) # 'e'

# Slicing
print(my_string[1:3]) # 'el'

# Step operator
print(my_string[::2]) # 'hlowrd'

# Reverse a string
print(my_string[::-1])

# Concatenate with '+'
greeting = 'Hello'
name = 'Tom'
print(greeting + ' ' + name)

# Iterate over string with for-in loop
for ch in 'helloworld':
  print(ch)

if "all" in "hallo":
  print("Yes")
else:
  print("No")

my_string = '    Hello World    '
print(my_string.strip())
my_string = my_string.strip()
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith('Hello'))
print(my_string.endswith('orld'))
print(my_string.find('or'))
print(my_string.find('z')) # -1
print(my_string.count('o')) # 2
print(my_string.replace('o', 'p'))

my_string = 'how are you doing'
my_list = my_string.split(' ')
print(my_list)

new_string = ' '.join(my_list)
print(new_string)

my_list = ['a'] * 6
print(my_list)

print(''.join(my_list))

my_list = ['a'] * 10000000

# Bad
start = timer()
my_string = ''
for i in my_list:
  my_string += i
stop = timer()
print(stop - start)

# Faster
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)

# String formatting

## Percent formatting
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)
var = 4
print("the variable is %d" % var)
var = 3.1415
print("the variable is %.2f" % var)

## Newer formatting style with dot-format
var = 3.1415
print("the variable is {}".format(var))
print("the variable is {:.2f}".format(var))
var2 = 6
print("the variable is {:.2f} and {}".format(var, var2))

## Newest using f-strings (since python 3.6)
var = 6.825
print(f"the variable is {var} and {var*2}")