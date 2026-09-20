# ==========================================
# Python Conditional Problems Practice
# ==========================================

print("🐍 PYTHON CONDITIONALS PRACTICE")
print("-" * 45)


# 1. Adult or Minor
print("\n1. Adult or Minor")

age = 22

if age >= 18:
    print("Adult")
else:
    print("Minor")


# 2. Positive, Negative or Zero
print("\n2. Positive, Negative or Zero")

number = -10

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 3. Even or Odd
print("\n3. Even or Odd")

number = 17

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")


# 4. Largest of Two Numbers
print("\n4. Largest of Two Numbers")

a = 40
b = 25

if a > b:
    print(a, "is larger")
elif b > a:
    print(b, "is larger")
else:
    print("Both are equal")


# 5. Largest of Three Numbers
print("\n5. Largest of Three Numbers")

a = 20
b = 80
c = 50

if a >= b and a >= c:
    print(a, "is largest")
elif b >= a and b >= c:
    print(b, "is largest")
else:
    print(c, "is largest")


# 6. Grade Calculator
print("\n6. Grade Calculator")

marks = 82

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print("Marks:", marks)
print("Grade:", grade)


# 7. Leap Year
print("\n7. Leap Year")

year = 2028

if year % 400 == 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 4 == 0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


# 8. Password Strength
print("\n8. Password Strength")

password = "Python@123"

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")


# 9. Movie Ticket Price
print("\n9. Movie Ticket Price")

age = 22

if age < 5:
    price = 0
elif age <= 12:
    price = 100
elif age >= 60:
    price = 120
else:
    price = 200

print("Age:", age)
print("Ticket Price: ₹", price)


# 10. Temperature Suggestion
print("\n10. Temperature Suggestion")

temperature = 28

if temperature >= 35:
    print("It's hot — stay hydrated.")
elif temperature >= 25:
    print("Good weather for outdoor activities.")
elif temperature >= 15:
    print("Weather is cool.")
else:
    print("It's cold — wear warm clothes.")


print("\n" + "-" * 45)
print("✅ 10 Conditional Problems Completed!")