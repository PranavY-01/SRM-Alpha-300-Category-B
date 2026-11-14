# Intermediate Python Course | Class 9. JSON
# -----------------------------------------------------------------------
import json
# -----------------------------------------------------------------------
# A. Python objects to JSON
# -----------------------------------------------------------------------

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"]
}

personJSON = json.dumps(person)

print(personJSON)
print(type(personJSON))

# -----------------------------------------------------------------------
# B. Pretty-printing JSON
# -----------------------------------------------------------------------

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"]
}

personJSON = json.dumps(person, indent=4)

print(personJSON)

# -----------------------------------------------------------------------
# C. JSON string to Python object
# -----------------------------------------------------------------------

personJSON = """
{
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": false,
    "titles": ["engineer", "programmer"]
}
"""

person = json.loads(personJSON)

print(person)
print(type(person))

# -----------------------------------------------------------------------
# D. Working with nested JSON
# -----------------------------------------------------------------------

person = {
    "name": "John",
    "address": {
        "street": "Main Street",
        "city": "New York"
    },
    "skills": ["Python", "Java", "C++"]
}

personJSON = json.dumps(person, indent=4)
print(personJSON)

# Access nested values
person_dict = json.loads(personJSON)

print(person_dict["address"]["city"])
print(person_dict["skills"][0])

# -----------------------------------------------------------------------
# E. Handling JSON errors
# -----------------------------------------------------------------------

import json

invalid_json = '{"name": "John", "age": 30,}'

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print("Invalid JSON:", e)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------