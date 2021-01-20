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