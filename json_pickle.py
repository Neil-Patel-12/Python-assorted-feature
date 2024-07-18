import jsonpickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the class
person = Person('Alice', 30)

# Serialize the object
person_json = jsonpickle.encode(person)
print(person_json)

# Deserialize the JSON back to an object
person_obj = jsonpickle.decode(person_json)
print(person_obj)
print(person_obj.name, person_obj.age)

"""
The main idea of using jsonpickle in Python is to enable serialization and deserialization
of complex Python objects to and from JSON. While the built-in json module in Python can handle
basic data types like dictionaries, lists, strings, numbers, and booleans, it struggles
with more complex objects like custom classes, objects with circular references,
and non-standard types. jsonpickle addresses these limitations by:

Serializing Complex Objects: It converts complex Python objects, including instances of
custom classes, into JSON-compatible format.

Deserializing JSON: It reconstructs the original Python objects from the JSON
representation, preserving the original types and structures.

Handling Circular References: It manages objects that reference themselves or each other,
which can cause issues with standard JSON serialization.

Customizability: It allows customization of the serialization and deserialization process
to fit specific needs.
"""