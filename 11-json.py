import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

print(json.dumps(person, indent=2))

# Specify different separators using `separators`
print(json.dumps(person, indent=2, separators=('; ', '= ')))

# User sort_keys to sort keys
print(json.dumps(person, indent=2, sort_keys=True))

with open('person.json', 'w') as file:
  json.dump(person, file, indent=2)