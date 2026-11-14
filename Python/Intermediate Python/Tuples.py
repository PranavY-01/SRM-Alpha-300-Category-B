# Intermediate Python Course | Class 2. Tuples
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Creating a tuple
# -----------------------------------------------------------------------

mytuple = ("Max", 28, "Boston")
print(mytuple)

mytuple = "Max", 28, "Boston"
print(mytuple)

mytuple = ("Max",)
print(mytuple)

mytuple = tuple()
print(mytuple)

mytuple = tuple([1, 2, 3])
print(mytuple)

not_a_tuple = (5)
is_a_tuple = (5,)

print(type(not_a_tuple))
print(type(is_a_tuple))

# -----------------------------------------------------------------------
# B. Accessing elements
# -----------------------------------------------------------------------

mytuple = ("Max", 28, "Boston")

# Indexing
print(mytuple[0])
print(mytuple[1])
print(mytuple[-1])

# Slicing
print(mytuple[0:2])
print(mytuple[::-1])

# -----------------------------------------------------------------------
# C. Iterating through a tuple
# -----------------------------------------------------------------------

mytuple = ("Max", 28, "Boston")

for item in mytuple:
    print(item)

# -----------------------------------------------------------------------
# D. Tuple length and counting
# -----------------------------------------------------------------------

mytuple = ("a", "p", "p", "l", "e")

# Number of elements
print(len(mytuple))

# Count occurrences
print(mytuple.count("p"))

# Find index of an element
print(mytuple.index("p"))

# -----------------------------------------------------------------------
# E. Tuple Unpacking
# -----------------------------------------------------------------------

mytuple = ("Max", 28, "Boston")

name, age, city = mytuple

print(name)
print(age)
print(city)

mytuple = (0, 1, 2, 3, 4, 5)

first, *middle, last = mytuple

print(first)
print(middle)
print(last)

# -----------------------------------------------------------------------
# F. Memory and performance
# -----------------------------------------------------------------------

import sys

my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)

print("List size:", sys.getsizeof(my_list), "bytes")
print("Tuple size:", sys.getsizeof(my_tuple), "bytes")