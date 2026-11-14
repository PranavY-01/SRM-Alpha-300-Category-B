# Intermediate Python Course | Class 5. Strings
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Creating a string
# -----------------------------------------------------------------------

my_string = "Hello World"
print(my_string)

my_string = 'Hello World'
print(my_string)

# Multiline string
my_string = """Hello
World"""
print(my_string)

# Empty string
my_string = ""
print(my_string)

# -----------------------------------------------------------------------
# B. String indexing and slicing
# -----------------------------------------------------------------------

greeting = "Hello"
name = "Tom"

sentence = greeting + " " + name
print(sentence)

my_string = "Hello"

for char in my_string:
    print(char)

# -----------------------------------------------------------------------
# C. Useful string methods
# -----------------------------------------------------------------------

my_string = "    Hello World    "

print(my_string.strip())

# Convert to uppercase
print(my_string.upper())

# Convert to lowercase
print(my_string.lower())

# Check whether string starts or ends with a value
print(my_string.startswith("    Hello"))
print(my_string.endswith("    "))

# Find substring position
print(my_string.find("World"))

# Count occurrences
print(my_string.count("o"))

# Replace substring
print(my_string.replace("World", "Tom"))

# -----------------------------------------------------------------------
# D. String formatting
# -----------------------------------------------------------------------

name = "Tom"
age = 25

# Old-style formatting
my_string = "The name is %s" % name
print(my_string)

# str.format()
my_string = "The name is {} and age is {}".format(name, age)
print(my_string)

# f-string
my_string = f"The name is {name} and age is {age}"
print(my_string)

# -----------------------------------------------------------------------
# String Checking Properties
# -----------------------------------------------------------------------

my_string = "Hello123"

print(my_string.isalpha())
print(my_string.isdigit())
print(my_string.isalnum())
print(my_string.isspace())
print(my_string.istitle())

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------