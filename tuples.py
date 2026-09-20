# ==========================================
# Python Tuples Practice
# ==========================================

print("🐍 PYTHON TUPLES PRACTICE")
print("-" * 45)

# 1. Creating a Tuple
languages = ("Python", "JavaScript", "Java")

print("\n1. Creating a Tuple")
print("Languages:", languages)
print("Type:", type(languages))


# 2. Accessing Tuple Items
print("\n2. Tuple Indexing")
print("First:", languages[0])
print("Second:", languages[1])
print("Last:", languages[-1])


# 3. Tuple Slicing
numbers = (10, 20, 30, 40, 50, 60)

print("\n3. Tuple Slicing")
print("Original:", numbers)
print("numbers[1:4]:", numbers[1:4])
print("numbers[:3]:", numbers[:3])
print("numbers[3:]:", numbers[3:])
print("Reverse:", numbers[::-1])


# 4. Tuples are Immutable
print("\n4. Tuple Immutability")

skills = ("Python", "React", "Node.js")
print("Original:", skills)

# skills[0] = "Java"
# TypeError: tuple does not support item assignment

print("Tuple values cannot be directly modified.")


# 5. Tuple Length
print("\n5. Tuple Length")
print("Total languages:", len(languages))


# 6. count()
values = (10, 20, 10, 30, 10, 40)

print("\n6. count()")
print("Tuple:", values)
print("10 appears:", values.count(10), "times")


# 7. index()
print("\n7. index()")
print("Index of 20:", values.index(20))
print("Index of 40:", values.index(40))


# 8. Membership
print("\n8. Membership")
print("Python exists:", "Python" in languages)
print("C++ exists:", "C++" in languages)


# 9. Loop Through Tuple
print("\n9. Loop Through Tuple")

for language in languages:
    print(language)


# 10. Single Item Tuple
print("\n10. Single Item Tuple")

single = ("Python",)
not_tuple = ("Python")

print("single:", single)
print("Type:", type(single))

print("not_tuple:", not_tuple)
print("Type:", type(not_tuple))


# 11. Tuple Packing
print("\n11. Tuple Packing")

developer = "Sachin", "Python", "Backend"

print("Packed Tuple:", developer)


# 12. Tuple Unpacking
print("\n12. Tuple Unpacking")

name, language, role = developer

print("Name:", name)
print("Language:", language)
print("Role:", role)


# 13. Extended Unpacking
print("\n13. Extended Unpacking")

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# 14. Concatenating Tuples
print("\n14. Tuple Concatenation")

frontend = ("HTML", "CSS", "JavaScript")
backend = ("Node.js", "MongoDB")

full_stack = frontend + backend

print("Full Stack:", full_stack)


# 15. Repeating Tuple
print("\n15. Repeating Tuple")

data = ("Python",) * 3

print(data)


# 16. Nested Tuple
print("\n16. Nested Tuple")

students = (
    ("Sachin", 90),
    ("Rahul", 85),
    ("Aman", 80)
)

print("Students:", students)
print("First Student:", students[0])
print("Sachin Marks:", students[0][1])


# 17. Tuple to List
print("\n17. Tuple → List")

skills = ("Python", "React", "Node.js")

skills_list = list(skills)
skills_list.append("MongoDB")

print("Original Tuple:", skills)
print("Converted List:", skills_list)


# 18. List Back to Tuple
print("\n18. List → Tuple")

updated_skills = tuple(skills_list)

print("Updated Tuple:", updated_skills)


# 19. min(), max(), sum()
print("\n19. Tuple Calculations")

marks = (75, 90, 85, 95, 80)

print("Minimum:", min(marks))
print("Maximum:", max(marks))
print("Total:", sum(marks))


# 20. Practical Example
print("\n20. Developer Profile")

profile = (
    "Sachin Kumar",
    "Python",
    "Learning"
)

name, technology, status = profile

print("Name:", name)
print("Technology:", technology)
print("Status:", status)


print("\n" + "-" * 45)
print("✅ Python Tuples Practice Completed!")