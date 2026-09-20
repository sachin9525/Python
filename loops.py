# ==========================================
# Python Loops - 10 Problems Practice
# ==========================================

print("🐍 PYTHON LOOPS PRACTICE")
print("-" * 45)


# ==========================================
# 1. Counting Positive Numbers
# ==========================================

print("\n1. Counting Positive Numbers")

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_count = 0

for number in numbers:
    if number > 0:
        positive_count += 1

print("Numbers:", numbers)
print("Positive numbers:", positive_count)


# ==========================================
# 2. Sum of Even Numbers
# ==========================================

print("\n2. Sum of Even Numbers")

number = 10
even_sum = 0

for i in range(1, number + 1):
    if i % 2 == 0:
        even_sum += i

print("Numbers from 1 to", number)
print("Sum of even numbers:", even_sum)


# ==========================================
# 3. Multiplication Table Printer
# ==========================================

print("\n3. Multiplication Table")

number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# ==========================================
# 4. Reverse a String
# ==========================================

print("\n4. Reverse a String")

text = "Python"

reversed_text = ""

for character in text:
    reversed_text = character + reversed_text

print("Original:", text)
print("Reversed:", reversed_text)


# ==========================================
# 5. First Non-Repeated Character
# ==========================================

print("\n5. First Non-Repeated Character")

text = "teeter"

for character in text:
    if text.count(character) == 1:
        print("First non-repeated character:", character)
        break
else:
    print("No non-repeated character found")


# ==========================================
# 6. Factorial Calculator
# ==========================================

print("\n6. Factorial Calculator")

number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Number:", number)
print("Factorial:", factorial)


# ==========================================
# 7. Validate Input
# ==========================================

print("\n7. Validate Input")

# Fixed values are used here so the complete
# practice file runs without waiting for input.

user_input = 7

while user_input < 1 or user_input > 10:
    print("Invalid input")
    user_input = 7

print("Valid input:", user_input)


# ==========================================
# 8. Prime Number Checker
# ==========================================

print("\n8. Prime Number Checker")

number = 29

if number <= 1:
    print(number, "is not a Prime Number")

else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a Prime Number")
    else:
        print(number, "is not a Prime Number")


# ==========================================
# 9. List Uniqueness Checker
# ==========================================

print("\n9. List Uniqueness Checker")

items = ["apple", "banana", "mango", "apple"]

duplicate_found = False

for item in items:

    if items.count(item) > 1:
        print("Duplicate found:", item)
        duplicate_found = True
        break

if not duplicate_found:
    print("All items are unique")

print("List:", items)


# ==========================================
# 10. Exponential Backoff
# ==========================================

print("\n10. Exponential Backoff")

max_retries = 5
wait_time = 1

for attempt in range(1, max_retries + 1):

    print(
        "Attempt:",
        attempt,
        "- Wait time:",
        wait_time,
        "seconds"
    )

    wait_time *= 2


# ==========================================
# Completed
# ==========================================

print("\n" + "-" * 45)
print("✅ 10 Python Loop Problems Completed!")