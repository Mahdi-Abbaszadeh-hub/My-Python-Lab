# Logs a message before and after the decorated function is called
def log_execution(func):
    def wrapper(*args, **kwargs):
        print("Function execution started")
        result = func(*args, **kwargs)
        print("Function execution finished")
        return result

    return wrapper


@log_execution
def say_hello():
    print("hi")


say_hello()

# --------------------------------


# Executes the decorated function only if the current minute is an even number
import datetime


def run_if_minute_is_even(func):
    def wrapper(*args, **kwargs):
        current_minute = datetime.datetime.now().minute
        if current_minute % 2 == 0:
            return func(*args, **kwargs)
        else:
            print("Access denied: The current minute is odd.")

    return wrapper


@run_if_minute_is_even
def say_hello():
    print("hi i'm here")


@run_if_minute_is_even
def say_bye():
    print("Bye Bye")


say_hello()
say_bye()

# --------------------------------


# Caches function results to avoid recalculating the same input
def memoize(func):
    cache = {}

    def wrapper(x):
        if x in cache:
            return cache[x]

        result = func(x)
        cache[x] = result
        return result

    return wrapper


@memoize
def square(x):
    print("calculating...")
    return x * x


print(square(5))
print(square(5))
print(square(6))

# --------------------------------


# Counts how many times the decorated function is called
def count_calls(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Call number {count}")
        return func(*args, **kwargs)

    return wrapper


@count_calls
def say_hi():
    print("hi")


say_hi()
say_hi()
say_hi()

# --------------------------------

import datetime

def run_if_even_minute(func):
    """
    A decorator that executes the decorated function only during even-numbered 
    minutes of the hour. Otherwise, it prints a 'hiss' message.
    """
    def wrapper(*args, **kwargs):
        current_minute = datetime.datetime.now().minute
        if current_minute % 2 == 0:
            return func(*args, **kwargs)
        else:
            print(f"[{current_minute}] Shhh! It's an odd minute.")
    return wrapper

@run_if_even_minute
def say_hello():
    """Prints a friendly greeting."""
    print("Hi i'm here!")

@run_if_even_minute
def say_bye():
    """Prints a farewell message."""
    print('Bye Bye!')

say_hello()
say_bye()

# --------------------------------
