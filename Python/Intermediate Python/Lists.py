# Intermediate Python Course | Class 1. Lists
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Creating a list
# -----------------------------------------------------------------------

fruits = ["banana", "cherry", "apple"]
print(fruits)

empty_list = list()
print(empty_list)

empty_list.append("orange")
print(empty_list)

mixed_list = [10, True, "Hello"]
print(mixed_list)

fruits = ["banana", "cherry", "apple", "apple"]
print(fruits)

# -----------------------------------------------------------------------
# B. Accessing elements
# -----------------------------------------------------------------------

fruits = ["banana", "cherry", "apple"]

# Positive indexing
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Negative indexing
print(fruits[-1])
print(fruits[-2])

# -----------------------------------------------------------------------
# C. Iterating through a list
# -----------------------------------------------------------------------

fruits = ["banana", "cherry", "apple"]

for fruit in fruits:
    print(fruit)

# -----------------------------------------------------------------------
# D. Checking whether an element exists
# -----------------------------------------------------------------------

fruits = ["banana", "cherry", "apple"]

if "banana" in fruits:
    print("Yes")
else:
    print("No")

if "lemon" in fruits:
    print("Yes")
else:
    print("No")

# -----------------------------------------------------------------------
# E. Useful list methods
# -----------------------------------------------------------------------

fruits = ["banana", "cherry", "apple"]

print(len(fruits))

fruits.append("lemon")
print(fruits)

fruits.insert(1, "blueberry")
print(fruits)

last_item = fruits.pop()
print(last_item)
print(fruits)

fruits.remove("cherry")
print(fruits)

fruits.clear()
print(fruits)

# -----------------------------------------------------------------------
# F. Reverse and Sort
# -----------------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

numbers = [4, 2, 3, 1, -1, -5, 10]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

original = [4, 2, 3, 1]
new_list = sorted(original)

print("Original:", original)
print("New:", new_list)

# -----------------------------------------------------------------------
# G. Repeating and concatenating lists
# -----------------------------------------------------------------------

zeros = [0] * 5
print(zeros)

numbers = [1, 2, 3, 4, 5]

combined = zeros + numbers
print(combined)

# -----------------------------------------------------------------------
# H. List slicing
# -----------------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = numbers[1:5]
print(a)

print(numbers[:5])

print(numbers[2:])

print(numbers[:])

print(numbers[::2])

print(numbers[::-1])

print(numbers[-4:-1])

# -----------------------------------------------------------------------
# I. Copying a list
# -----------------------------------------------------------------------

original = ["banana", "cherry", "apple"]

copy_one = original.copy()  # Method 1: copy()

copy_two = list(original)   # Method 2: list()

copy_three = original[:]    # Method 3: slicing

copy_one.append("lemon")

print("Original:", original)
print("Copy one:", copy_one)
print("Copy two:", copy_two)
print("Copy three:", copy_three)

# -----------------------------------------------------------------------
# J. List comprehension
# -----------------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

squared_numbers = [number * number for number in numbers]

print("Original:", numbers)
print("Squared:", squared_numbers)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
