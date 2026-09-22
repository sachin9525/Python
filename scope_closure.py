# ==========================================
# Python Scope and Closures Practice
# ==========================================

print("🐍 PYTHON SCOPE & CLOSURES PRACTICE")
print("-" * 45)


# 1. Local Scope
print("\n1. Local Scope")

def local_scope():
    message = "I am a local variable"
    print(message)

local_scope()


# 2. Global Scope
print("\n2. Global Scope")

language = "Python"

def show_language():
    print("Language:", language)

show_language()


# 3. Local vs Global Variable
print("\n3. Local vs Global Variable")

name = "Global Sachin"

def show_name():
    name = "Local Sachin"
    print("Inside function:", name)

show_name()
print("Outside function:", name)


# 4. global Keyword
print("\n4. global Keyword")

count = 10

def update_count():
    global count
    count = 20

update_count()

print("Updated global count:", count)


# 5. Nested Function
print("\n5. Nested Function")

def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()


# 6. nonlocal Keyword
print("\n6. nonlocal Keyword")

def counter():

    value = 0

    def increment():
        nonlocal value
        value += 1
        return value

    print(increment())
    print(increment())
    print(increment())

counter()


# 7. Basic Closure
print("\n7. Basic Closure")

def outer_function(message):

    def inner_function():
        print(message)

    return inner_function


hello = outer_function("Hello from Closure!")

hello()


# 8. Closure Remembers Data
print("\n8. Closure Remembers Data")

def multiplier(number):

    def multiply(value):
        return number * value

    return multiply


double = multiplier(2)
triple = multiplier(3)

print("Double 5:", double(5))
print("Triple 5:", triple(5))


# 9. Independent Closures
print("\n9. Independent Closures")

def create_counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter_one = create_counter()
counter_two = create_counter()

print("Counter One:", counter_one())
print("Counter One:", counter_one())

print("Counter Two:", counter_two())

print("Counter One:", counter_one())


# 10. LEGB Rule
print("\n10. LEGB Rule")

value = "Global"

def outer_scope():

    value = "Enclosing"

    def inner_scope():

        value = "Local"

        print("Inside inner:", value)

    inner_scope()

    print("Inside outer:", value)


outer_scope()

print("Outside:", value)


print("\n" + "-" * 45)
print("✅ Python Scope & Closures Practice Completed!")