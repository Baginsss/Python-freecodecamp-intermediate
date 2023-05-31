import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

with open('person.json', 'r') as file:
    person = json.loads(personJSON)
    print(person)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

def encode_user(object):
    if isinstance(object, User):
        return {'name': object.name, 'age': object.age, object.__class__.__name__: True}
    else:
        raise TypeError('Object of type user is not JSON serializable')

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, User):
            return {'name': object.name, 'age': object.age, object.__class__.__name__: True}
        return JSONEncoder.default(self, object)

userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

userJSON = UserEncoder().encode(user)
print(userJSON)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)
