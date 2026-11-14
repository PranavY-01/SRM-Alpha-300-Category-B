# Object-Oriented Programming in Python Course | Class 1. Getting Started 5. OOP Principles
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Encapsulation
# -----------------------------------------------------------------------
class Item:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.__price = price
        self.quantity = quantity

# -----------------------------------------------------------------------
# B. Creating a property for price
# -----------------------------------------------------------------------

@property
def price(self):
    return self.__price

# -----------------------------------------------------------------------
# C. Incrementing the price
# -----------------------------------------------------------------------

def apply_increment(self, increment_value):
    self.__price = self.__price + self.__price * increment_value

# -----------------------------------------------------------------------
# D. Applying a discount
# -----------------------------------------------------------------------

def apply_discount(self):
    self.__price = self.__price * self.pay_rate

# -----------------------------------------------------------------------
# E. Testing  (main.py)
# -----------------------------------------------------------------------

item1 = Item("MyItem", 750)
item1.apply_increment(0.2)
print(item1.price)

# -----------------------------------------------------------------------
# F. Abstraction
# -----------------------------------------------------------------------

class Item:
    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        pass

    def __send(self):
        pass

    def send_email(self):
        self.__connect("smtp.example.com")
        self.__prepare_body()
        self.__send()

# -----------------------------------------------------------------------
# G. Calling the email method
# -----------------------------------------------------------------------

item1 = Item("MyItem", 750)

item1.send_email()

# -----------------------------------------------------------------------
# H. Inheritance - reusing Item functionality
# -----------------------------------------------------------------------

class Phone(Item):
    pass

class Laptop(Item):
    pass

# -----------------------------------------------------------------------
# I. Applying inherited methods
# -----------------------------------------------------------------------

phone1 = Phone("iPhone 10", 500, 5)

phone1.apply_increment(0.2)

print(phone1.price)

# -----------------------------------------------------------------------
# J. Polymorphism - using the same method name for different classes: Keyboard
# -----------------------------------------------------------------------

class Keyboard(Item):
    pay_rate = 0.7

# -----------------------------------------------------------------------
# K. Applying different discount rates
# -----------------------------------------------------------------------

phone1 = Phone("iPhone 10", 500, 5)
keyboard1 = Keyboard("Keyboard", 100, 10)

phone1.apply_discount()
keyboard1.apply_discount()

print(phone1.price)
print(keyboard1.price)

# -----------------------------------------------------------------------
# L. Controlling class-specific discount rates
# -----------------------------------------------------------------------

class Phone(Item):
    pay_rate = 0.5

class Keyboard(Item):
    pay_rate = 0.7


# -----------------------------------------------------------------------
# M. Overriding the class attribute
# -----------------------------------------------------------------------

class Keyboard(Item):
    pay_rate = 0.3

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
