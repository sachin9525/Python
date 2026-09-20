# ==========================================
# Python Dictionary Practice
# ==========================================

print("🐍 PYTHON DICTIONARY PRACTICE")
print("-" * 45)

# 1. Creating a Dictionary
student = {
    "name": "Sachin Kumar",
    "course": "Python",
    "age": 24
}

print("\n1. Creating Dictionary")
print(student)


# 2. Accessing Values
print("\n2. Accessing Values")
print("Name:", student["name"])
print("Course:", student["course"])


# 3. Using get()
print("\n3. Using get()")
print("Age:", student.get("age"))
print("City:", student.get("city", "Not Available"))


# 4. Adding New Key-Value Pair
print("\n4. Adding New Data")

student["city"] = "Bhopal"

print(student)


# 5. Updating Values
print("\n5. Updating Values")

student["course"] = "Advanced Python"

print(student)


# 6. keys()
print("\n6. Dictionary Keys")

print(student.keys())


# 7. values()
print("\n7. Dictionary Values")

print(student.values())


# 8. items()
print("\n8. Dictionary Items")

print(student.items())


# 9. Loop Through Dictionary
print("\n9. Loop Through Dictionary")

for key, value in student.items():
    print(f"{key}: {value}")


# 10. Check Key
print("\n10. Checking Keys")

print("name" in student)
print("email" in student)


# 11. Dictionary Length
print("\n11. Dictionary Length")

print("Total key-value pairs:", len(student))


# 12. pop()
print("\n12. pop()")

removed_age = student.pop("age")

print("Removed Age:", removed_age)
print("Updated Dictionary:", student)


# 13. Copy Dictionary
print("\n13. Dictionary Copy")

original = {
    "Python": 90,
    "JavaScript": 85
}

copied = original.copy()
copied["React"] = 88

print("Original:", original)
print("Copied:", copied)


# 14. Nested Dictionary
print("\n14. Nested Dictionary")

students = {
    "student1": {
        "name": "Sachin",
        "marks": 90
    },
    "student2": {
        "name": "Rahul",
        "marks": 85
    }
}

print(students)

print("Student 1 Name:", students["student1"]["name"])
print("Student 2 Marks:", students["student2"]["marks"])


# 15. Dictionary Comprehension
print("\n15. Dictionary Comprehension")

squares = {
    number: number ** 2
    for number in range(1, 6)
}

print("Squares:", squares)


# 16. Create Dictionary From Lists
print("\n16. Creating Dictionary From Lists")

keys = ["name", "language", "level"]
values = ["Sachin", "Python", "Beginner"]

profile = dict(zip(keys, values))

print(profile)


# 17. update()
print("\n17. update()")

profile.update({
    "level": "Intermediate",
    "learning": True
})

print(profile)


# 18. setdefault()
print("\n18. setdefault()")

profile.setdefault("country", "India")
profile.setdefault("name", "Another Name")

print(profile)


# 19. fromkeys()
print("\n19. fromkeys()")

subjects = ["Python", "DSA", "SQL"]

progress = dict.fromkeys(subjects, "Learning")

print(progress)


# 20. Practical Example
print("\n20. Developer Profile")

developer = {
    "name": "Sachin Kumar",
    "skills": ["Python", "JavaScript", "React", "Node.js"],
    "learning_python": True
}

print("Developer:", developer["name"])
print("Skills:", developer["skills"])

for skill in developer["skills"]:
    print("-", skill)


print("\n" + "-" * 45)
print("✅ Python Dictionary Practice Completed!")