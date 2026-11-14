# Intermediate Python Course | Class 3. Dictionaries
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Creating a dictionary
# -----------------------------------------------------------------------

mydict = {
    "name": "Max",
    "age": 28,
    "city": "New York"
}

print(mydict)

# Creating an empty dictionary
mydict = dict()
print(mydict)

# Creating using dict()
mydict = dict(name="Mary", age=27, city="Boston")
print(mydict)

# -----------------------------------------------------------------------
# B. Accessing values
# -----------------------------------------------------------------------

mydict = {
    "name": "Max",
    "age": 28,
    "city": "New York"
}

# Access using keys
print(mydict["name"])
print(mydict["age"])

# Using get()
print(mydict.get("name"))
print(mydict.get("email"))

# Providing a default value
print(mydict.get("email", "Not found"))

# -----------------------------------------------------------------------
# C. Adding and updating elements
# -----------------------------------------------------------------------

mydict = {
    "name": "Max",
    "age": 28
}

# Add a new key-value pair
mydict["email"] = "max@example.com"

# Update an existing value
mydict["age"] = 29

print(mydict)

# -----------------------------------------------------------------------
# D. Removing elements
# -----------------------------------------------------------------------

mydict = {
    "name": "Max",
    "age": 28,
    "city": "New York"
}

# Remove a key-value pair using del
del mydict["age"]

print(mydict)

# -----------------------------------------------------------------------
# E. Iterating through a dictionary
# -----------------------------------------------------------------------

mydict = {
    "name": "Max",
    "age": 28,
    "city": "New York"
}

# Iterate through keys
for key in mydict:
    print(key)

# Iterate through keys explicitly
for key in mydict.keys():
    print(key)

# Iterate through values
for value in mydict.values():
    print(value)

# Iterate through key-value pairs
for key, value in mydict.items():
    print(key, value)

# -----------------------------------------------------------------------
# F. Create an independent shallow copy
# -----------------------------------------------------------------------

mydict = {
    "name": "Max",
    "age": 28
}

# Method 1
mydict_copy = mydict.copy()

# Method 2
mydict_copy = dict(mydict)

mydict_copy["name"] = "Anna"

print("Original:", mydict)
print("Copy:", mydict_copy)

# -----------------------------------------------------------------------
# G. Dictionary Comprehension
# -----------------------------------------------------------------------

mydict = {i: i * i for i in range(5)}

print(mydict)

# -----------------------------------------------------------------------