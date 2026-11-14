# Object-Oriented Programming in Python Course | Class 1. Getting Started
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Constructor using __init__
# -----------------------------------------------------------------------

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# -----------------------------------------------------------------------
# B. Creating instances with constructor arguments
# -----------------------------------------------------------------------

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

print(item1.name)
print(item2.name)

# -------------------------------------------------------------------------
# C. Default parameter values
# -------------------------------------------------------------------------

class Item:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

item1 = Item("Phone", 100)
item2 = Item("Laptop", 1000, 3)

print(item1.quantity)
print(item2.quantity)

# -------------------------------------------------------------------------
# D. Validating received arguments using assert
# -------------------------------------------------------------------------

class Item:
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

# -------------------------------------------------------------------------
# E. Using __repr__ to represent instances
# -------------------------------------------------------------------------

class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0
        assert quantity >= 0

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

print(Item.all)


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------