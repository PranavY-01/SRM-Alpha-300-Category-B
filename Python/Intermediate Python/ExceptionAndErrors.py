# Intermediate Python Course | Class 8. Exception and Errors
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Basic exception handling
# -----------------------------------------------------------------------

try:
    a = 5 / 0
except:
    print("An error happened")

# -----------------------------------------------------------------------
# B. Catching specific exceptions
# -----------------------------------------------------------------------

try:
    a = 5 / 0
except Exception as e:
    print(e)

# -----------------------------------------------------------------------
# C. Catching different exception types together
# -----------------------------------------------------------------------

try:
    a = 5 / 0
except (ZeroDivisionError, TypeError) as e:
    print(e)

# -----------------------------------------------------------------------
# D. Using else and finally
# -----------------------------------------------------------------------

try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(e)
finally:
    print("Cleaning up...")

# -----------------------------------------------------------------------
# E. Raising exceptions
# -----------------------------------------------------------------------

x = -5

if x < 0:
    raise Exception("x should be positive")

# -----------------------------------------------------------------------
# F. Creating custom exceptions
# -----------------------------------------------------------------------

class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------