# Intermediate Python Course | Class 10. Decorators
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Creating a decorator
# -----------------------------------------------------------------------

def start_end_decorator(func):

    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


def print_name():
    print("Alex")


decorated_function = start_end_decorator(print_name)

decorated_function()

# -----------------------------------------------------------------------
# B. Using the @ symbol
# -----------------------------------------------------------------------

@start_end_decorator
def print_new_name():
    print("Ben")

print_new_name()

# -----------------------------------------------------------------------
# C. Decorators with arguments
# -----------------------------------------------------------------------

import functools

def repeat(num_times):

    def decorator_repeat(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


greet("Alex")

# -----------------------------------------------------------------------
# D. Nested decorators
# -----------------------------------------------------------------------

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result

    return wrapper


def debug_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper

@start_end_decorator
@debug_decorator

def say_hello():
    print("Hello")

say_hello()

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------