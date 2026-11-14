# Object-Oriented Programming in Python Course | Class 3. Inheritance
# -----------------------------------------------------------------------
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
# -----------------------------------------------------------------------
# A. Creating an instance
# -----------------------------------------------------------------------

class Phone(Item):
    pass

phone1 = Phone("iPhone 10", 500, 5)
phone2 = Phone("Samsung Galaxy S10", 400, 5)

print(phone1.name)
print(phone2.name)

# -----------------------------------------------------------------------
# B. Adding additional attributes to the child class
# -----------------------------------------------------------------------

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        assert price >= 0
        assert quantity >= 0
        assert broken_phones >= 0

        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones

        Phone.all.append(self)

# -----------------------------------------------------------------------
# C. Using inherited methods
# -----------------------------------------------------------------------

print(phone1.calculate_total_price())
print(phone2.calculate_total_price())

# -----------------------------------------------------------------------
# D. Creating instances using the updated child class
# -----------------------------------------------------------------------

phone1 = Phone("iPhone 10", 500, 5, 1)
phone2 = Phone("Samsung Galaxy S10", 400, 5, 1)

print(phone1.calculate_total_price())
print(phone2.calculate_total_price())

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------