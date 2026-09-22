# ==========================================
# Python Decorators Practice
# ==========================================

import time
from functools import wraps

print("🐍 PYTHON DECORATORS PRACTICE")
print("-" * 45)


# 1. Function as an Object
print("\n1. Function as an Object")

def greet():
    return "Hello, Sachin!"

message = greet

print(message())


# 2. Function Inside Function
print("\n2. Function Inside Function")

def outer():

    def inner():
        return "Hello from inner function"

    return inner()


print(outer())


# 3. Returning a Function
print("\n3. Returning a Function")

def outer_function():

    def inner_function():
        return "Inner function executed"

    return inner_function


result = outer_function()

print(result())


# 4. Basic Decorator
print("\n4. Basic Decorator")

def my_decorator(func):

    def wrapper():
        print("Before function execution")

        func()

        print("After function execution")

    return wrapper


@my_decorator
def say_hello():
    print("Hello Python!")


say_hello()


# 5. Decorator with Arguments
print("\n5. Decorator with Arguments")

def decorator_with_arguments(func):

    def wrapper(*args, **kwargs):

        print("Function started")

        result = func(*args, **kwargs)

        print("Function completed")

        return result

    return wrapper


@decorator_with_arguments
def add(a, b):
    return a + b


print("Result:", add(10, 20))


# 6. Timing Function Execution
print("\n6. Timing Function Execution")

def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        print(
            f"{func.__name__} execution time: "
            f"{end_time - start_time:.6f} seconds"
        )

        return result

    return wrapper


@timer
def calculate():

    total = 0

    for number in range(1_000_000):
        total += number

    return total


print("Result:", calculate())


# 7. Debugging Function Calls
print("\n7. Debugging Function Calls")

def debug(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print("Function Name:", func.__name__)
        print("Arguments:", args)
        print("Keyword Arguments:", kwargs)

        result = func(*args, **kwargs)

        print("Returned:", result)

        return result

    return wrapper


@debug
def multiply(a, b):
    return a * b


multiply(5, 4)


# 8. Authentication Decorator
print("\n8. Authentication Decorator")

def login_required(func):

    @wraps(func)
    def wrapper(user):

        if user == "Sachin":
            return func(user)

        return "Access Denied"

    return wrapper


@login_required
def dashboard(user):
    return f"Welcome {user} to Dashboard"


print(dashboard("Sachin"))
print(dashboard("Rahul"))


# 9. Multiple Decorators
print("\n9. Multiple Decorators")

def first_decorator(func):

    def wrapper():
        print("First Decorator")
        func()

    return wrapper


def second_decorator(func):

    def wrapper():
        print("Second Decorator")
        func()

    return wrapper


@first_decorator
@second_decorator
def python_learning():
    print("Learning Python")


python_learning()


# 10. Decorator with Parameter
print("\n10. Decorator with Parameter")

def repeat(times):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def hello(name):
    print("Hello", name)


hello("Sachin")


# 11. Cache Return Values
print("\n11. Cache Return Values")

def cache(func):

    cached_values = {}

    @wraps(func)
    def wrapper(*args):

        if args in cached_values:
            print("Returning cached result")
            return cached_values[args]

        print("Calculating result")

        result = func(*args)

        cached_values[args] = result

        return result

    return wrapper


@cache
def square(number):
    return number * number


print(square(5))
print(square(5))
print(square(10))
print(square(10))


print("\n" + "-" * 45)
print("✅ PYTHON DECORATORS PRACTICE COMPLETED!")