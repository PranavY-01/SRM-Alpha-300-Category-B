# Object-Oriented Programming in Python Course | Class 4. Getter and Setter Methods
# -----------------------------------------------------------------------
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


item1 = Item("My Item", 750)

item1.name = "Other Item"

print(item1.name)

# -----------------------------------------------------------------------
# A. Creating a property
# -----------------------------------------------------------------------

@property
def read_only_name(self):
    return "AAA"

# -----------------------------------------------------------------------
# B. Using a single underscore
# -----------------------------------------------------------------------

class Item:
    def __init__(self, name, price, quantity=0):
        self._name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self._name

# -----------------------------------------------------------------------
# C. Using a double underscore
# -----------------------------------------------------------------------

class Item:
    def __init__(self, name, price, quantity=0):
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

# -----------------------------------------------------------------------
# D. Creating a setter method
# -----------------------------------------------------------------------

@property
def name(self):
    return self.__name

@name.setter
def name(self, value):
    self.__name = value

# -----------------------------------------------------------------------
# E. Tracking getter and setter execution
# -----------------------------------------------------------------------

@property
def name(self):
    print("You are trying to get name")
    return self.__name

@name.setter
def name(self, value):
    print("You are trying to set name")
    self.__name = value

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

