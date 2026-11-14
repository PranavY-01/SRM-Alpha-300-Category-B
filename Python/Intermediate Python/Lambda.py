# Intermediate Python Course | Class 7. Lambda Functions
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Creating a lambda function
# -----------------------------------------------------------------------

from functools import reduce


add10 = lambda x: x + 10

print(add10(5))

# -----------------------------------------------------------------------
# B. With conditional expressions
# -----------------------------------------------------------------------

check_even = lambda x: True if x % 2 == 0 else False

print(check_even(4))
print(check_even(5))

# -----------------------------------------------------------------------
# C. With sorted()
# -----------------------------------------------------------------------

points2D = [(1, 9), (4, 1), (5, -3), (10, 2)]

points2D_sorted = sorted(points2D)

print(points2D_sorted)

points2D_sorted = sorted(points2D, key=lambda x: x[1])

print(points2D_sorted)

# -----------------------------------------------------------------------
# D. With map()
# -----------------------------------------------------------------------

a = [1, 2, 3, 4, 5]

# Normal function
def add10(x):
    return x + 10

result = map(add10, a)
print(list(result))

# Using lambda
result = map(lambda x: x + 10, a)
print(list(result))

# -----------------------------------------------------------------------
# E. With filter()
# -----------------------------------------------------------------------

a = [1, 2, 3, 4, 5, 6]

# Normal function
def is_even(x):
    return x % 2 == 0

result = filter(is_even, a)
print(list(result))

# Using lambda
result = filter(lambda x: x % 2 == 0, a)
print(list(result))

# -----------------------------------------------------------------------
# F. With reduce()
# -----------------------------------------------------------------------

a = [1, 2, 3, 4, 5, 6]

# Normal function
def multiply(x, y):
    return x * y

result = reduce(multiply, a)
print(result)

# Using lambda
result = reduce(lambda x, y: x * y, a)
print(result)

# Using lambda
result = reduce(lambda x, y: x * y, a)
print(result)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------