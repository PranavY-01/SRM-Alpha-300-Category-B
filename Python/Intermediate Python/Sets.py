# Intermediate Python Course | Class 4. Sets
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Creating a set
# -----------------------------------------------------------------------

myset = {1, 2, 3}
print(myset)

# Duplicate elements are automatically removed
myset = {1, 2, 2, 3, 3, 3}
print(myset)

# Creating an empty set
myset = set()
print(myset)

# Creating a set from a list
myset = set([1, 2, 3, 4])
print(myset)

# Creating a set from a string
myset = set("Hello")
print(myset)

# -----------------------------------------------------------------------
# B. Adding and removing elements
# -----------------------------------------------------------------------

myset = {1, 2, 3}

# Add an element
myset.add(4)
print(myset)

# Remove an element
myset.remove(3)
print(myset)

# Discard an element
myset.discard(5)
print(myset)

# Remove and return an arbitrary element
myset.pop()
print(myset)

# Clear the set
myset.clear()
print(myset)

# -----------------------------------------------------------------------
# C. Set Union
# -----------------------------------------------------------------------

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

u = odds | evens
print(u)

# -----------------------------------------------------------------------
# D. Set Intersection
# -----------------------------------------------------------------------

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

i = odds.intersection(primes)
print(i)

i = odds & primes
print(i)

# -----------------------------------------------------------------------
# E. Set Difference
# -----------------------------------------------------------------------

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3, 7, 8, 9}

diff = setA.difference(setB)
print(diff)

diff = setA - setB
print(diff)

# -----------------------------------------------------------------------
# F. Set Symmetric Difference
# -----------------------------------------------------------------------

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3, 7, 8, 9}

diff = setA.symmetric_difference(setB)
print(diff)

diff = setA ^ setB
print(diff)

# -----------------------------------------------------------------------
# G. Frozen sets
# -----------------------------------------------------------------------

a = frozenset([1, 2, 3, 4])

print(a)

# This would raise AttributeError:
# a.add(5)

# Frozen sets can be dictionary keys
mydict = {a: "Numbers"}

print(mydict[a])

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------