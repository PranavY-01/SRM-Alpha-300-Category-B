# Intermediate Python Course | Class 11. Generators
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Creating a generator
# -----------------------------------------------------------------------

def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

print(g)

for i in g:
    print(i)

# -----------------------------------------------------------------------
# B. Using the next() function
# -----------------------------------------------------------------------

values = mygenerator()

print(next(values))
print(next(values))
print(next(values))

# -----------------------------------------------------------------------
# C. Generator expressions
# -----------------------------------------------------------------------

# List comprehension
mylist = [i for i in range(10)]
print(mylist)

# Generator expression
mygenerator = (i for i in range(10))
print(mygenerator)

for value in mygenerator:
    print(value)

# -----------------------------------------------------------------------
# D. Countdown generator
# -----------------------------------------------------------------------

def countdown(num):

    print('Starting')

    while num > 0:
        yield num
        num -= 1

cd = countdown(3)
    
values = next(cd)
print(values)

print(next(cd))
print(next(cd))

# -----------------------------------------------------------------------
# E. Memory Comparison
# -----------------------------------------------------------------------

import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append (num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sys.getsizeof(firstn(1000)))              # Output: 8856
print(sys.getsizeof(firstn_generator(1000)))    # Output: 192

# -----------------------------------------------------------------------
# ----------------------------------------------------------------------- 