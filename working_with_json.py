import json

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

c = Cat("Charles", "Tabby")

# json.dumps formats a python object as a STRING of JSON.
# it didn't do a good job of emphasizing the fact that it returns a STRING.
j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

j2 = json.dumps(c.__dict__)

print(j)
print(j2)

# python -m pip install jsonpickle