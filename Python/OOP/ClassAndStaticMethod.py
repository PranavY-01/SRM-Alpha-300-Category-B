# Object-Oriented Programming in Python Course | Class 2. Class and Static Methods
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Creating a class method
# -----------------------------------------------------------------------

@classmethod
def instantiate_from_csv(cls):
    pass

# -----------------------------------------------------------------------
# B. Reading a csv method
# -----------------------------------------------------------------------

import csv

from Python.OOP.GettingStarted import Item

@classmethod
def instantiate_from_csv(cls):
    with open('items.csv', 'r') as f:
        reader = csv.DictReader(f)
        items = list(reader)

    for item in items:
        print(item)

# -----------------------------------------------------------------------
# C. Creating instances from CSV data
# -----------------------------------------------------------------------

import csv

@classmethod
def instantiate_from_csv(cls):
    with open('items.csv', 'r') as f:
        reader = csv.DictReader(f)
        items = list(reader)

    for item in items:
        Item(
            name=item.get('name'),
            price=float(item.get('price')),
            quantity=int(item.get('quantity'))
        )

Item.instantiate_from_csv()

# -----------------------------------------------------------------------
# D. Creating a static method
# -----------------------------------------------------------------------

@staticmethod
def is_integer(num):
    if isinstance(num, float):
        return num.is_integer()
    elif isinstance(num, int):
        return True
    else:
        return False

# -----------------------------------------------------------------------
# E. Calling methods through an instance
# -----------------------------------------------------------------------

item1 = Item("Phone", 100, 5)

print(item1.is_integer(7))
item1.instantiate_from_csv()

# -----------------------------------------------------------------------
# F. Comparing class methods and static methods
# -----------------------------------------------------------------------

class Item:
    @classmethod
    def instantiate_from_csv(cls):
        pass

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
