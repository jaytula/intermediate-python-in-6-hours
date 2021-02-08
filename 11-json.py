import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=2)
print(personJSON)

# Specify different separators using `separators`
print(json.dumps(person, indent=2, separators=('; ', '= ')))

# User sort_keys to sort keys
print(json.dumps(person, indent=2, sort_keys=True))

with open('person.json', 'w') as file:
  json.dump(person, file, indent=2)

# Convert string back to python dictionary using json.loads
person = json.loads(personJSON)
print(person)

# Convert JSON file to python dictionary
with open('person.json', 'r') as file:
  person = json.load(file)
  print(person)

# Example of encoding custom object to JSON
class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age

user = User('Max', 27)

def encode_user(o):
  if isinstance(o, User):
    return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
  else:
    raise TypeError('Boject of type User is not JSON serializable')

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

from json import JSONEncoder

class UserEncoder(JSONEncoder):
  def default(self, o):
    if isinstance(o, User):
      return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

userJSON = UserEncoder().encode(user)
print(userJSON)

# Decode back into an object. Need to write a custom decoder

def decode_user(dct):
  if User.__name__ in dct:
    return User(name=dct['name'], age=dct['age'])
  return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user)) # <class '__main__.User'>
print(user.name)