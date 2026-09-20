# ==========================================
# Python Functions - 10 Problems Practice
# ==========================================

print("🐍 PYTHON FUNCTIONS PRACTICE")
print("-" * 45)


# 1. Square of a Number
print("\n1. Square of a Number")

def square(number):
    return number ** 2

print("Square of 5:", square(5))


# 2. Sum of Two Numbers
print("\n2. Sum of Two Numbers")

def add(a, b):
    return a + b

print("10 + 20 =", add(10, 20))


# 3. Multiply Two Numbers
print("\n3. Multiply Two Numbers")

def multiply(a, b):
    return a * b

print("5 × 6 =", multiply(5, 6))


# 4. Circle Area and Circumference
print("\n4. Circle Area and Circumference")

def circle(radius):
    area = 3.14159 * radius ** 2
    circumference = 2 * 3.14159 * radius
    return area, circumference

area, circumference = circle(5)

print("Area:", round(area, 2))
print("Circumference:", round(circumference, 2))


# 5. Greeting with Default Parameter
print("\n5. Default Parameter")

def greet(name="User"):
    return "Hello, " + name + "!"

print(greet("Sachin"))
print(greet())


# 6. Lambda Function
print("\n6. Lambda Function")

cube = lambda number: number ** 3

print("Cube of 4:", cube(4))


# 7. Sum using *args
print("\n7. Using *args")

def total_sum(*numbers):
    return sum(numbers)

print("Total:", total_sum(10, 20, 30, 40))


# 8. Function using **kwargs
print("\n8. Using **kwargs")

def show_profile(**details):
    for key, value in details.items():
        print(key, ":", value)

show_profile(
    name="Sachin",
    language="Python",
    level="Beginner"
)


# 9. Even or Odd Function
print("\n9. Even or Odd")

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

print("17 is", check_even_odd(17))
print("20 is", check_even_odd(20))


# 10. Factorial using Function
print("\n10. Factorial using Function")

def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

print("Factorial of 5:", factorial(5))


# ==========================================
# Completed
# ==========================================

print("\n" + "-" * 45)
print("✅ 10 Python Function Problems Completed!")