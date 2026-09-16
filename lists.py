# ==========================================
# Python Lists Practice
# ==========================================

print("🐍 PYTHON LISTS PRACTICE")
print("-" * 45)

# 1. Creating a List
fruits = ["Apple", "Banana", "Mango"]

print("\n1. Creating a List")
print("Fruits:", fruits)


# 2. Accessing List Items
print("\n2. List Indexing")
print("First item:", fruits[0])
print("Second item:", fruits[1])
print("Last item:", fruits[-1])


# 3. List Slicing
numbers = [10, 20, 30, 40, 50, 60]

print("\n3. List Slicing")
print("Original:", numbers)
print("numbers[1:4]:", numbers[1:4])
print("numbers[:3]:", numbers[:3])
print("numbers[3:]:", numbers[3:])
print("Reverse:", numbers[::-1])


# 4. Lists are Mutable
print("\n4. List Mutability")

fruits[1] = "Orange"
print("After modification:", fruits)


# 5. append()
print("\n5. append()")

fruits.append("Grapes")
print(fruits)


# 6. insert()
print("\n6. insert()")

fruits.insert(1, "Watermelon")
print(fruits)


# 7. remove()
print("\n7. remove()")

fruits.remove("Mango")
print(fruits)


# 8. pop()
print("\n8. pop()")

removed_item = fruits.pop()

print("Removed:", removed_item)
print("Updated:", fruits)


# 9. List Length
print("\n9. List Length")
print("Total items:", len(fruits))


# 10. Check Membership
print("\n10. Membership")

print("Apple exists:", "Apple" in fruits)
print("Mango exists:", "Mango" in fruits)


# 11. Loop Through List
print("\n11. Loop Through List")

for fruit in fruits:
    print(fruit)


# 12. Copying a List
print("\n12. Copying Lists")

original = ["Python", "JavaScript", "React"]

copied = original.copy()
copied.append("Node.js")

print("Original:", original)
print("Copied  :", copied)


# 13. Assignment vs Copy
print("\n13. Assignment vs Copy")

list_one = [1, 2, 3]
list_two = list_one

list_two.append(4)

print("List One:", list_one)
print("List Two:", list_two)

print("Same object:", list_one is list_two)


# 14. Sorting
print("\n14. Sorting")

marks = [85, 60, 95, 70, 80]

print("Original:", marks)

marks.sort()
print("Ascending:", marks)

marks.sort(reverse=True)
print("Descending:", marks)


# 15. min(), max(), sum()
print("\n15. List Calculations")

numbers = [10, 20, 30, 40, 50]

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Total:", sum(numbers))


# 16. count()
print("\n16. count()")

values = [10, 20, 10, 30, 10, 40]

print("List:", values)
print("10 appears:", values.count(10), "times")


# 17. index()
print("\n17. index()")

languages = ["Python", "Java", "JavaScript"]

print("Python index:", languages.index("Python"))
print("JavaScript index:", languages.index("JavaScript"))


# 18. extend()
print("\n18. extend()")

frontend = ["HTML", "CSS"]
backend = ["Node.js", "Express.js"]

frontend.extend(backend)

print("Combined:", frontend)


# 19. List Comprehension
print("\n19. List Comprehension")

squares = [x * x for x in range(1, 6)]

print("Squares:", squares)


# 20. Filter Using List Comprehension
print("\n20. Even Numbers")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [x for x in numbers if x % 2 == 0]

print("Original:", numbers)
print("Even:", even_numbers)


# 21. Nested List
print("\n21. Nested List")

students = [
    ["Sachin", 85],
    ["Rahul", 90],
    ["Aman", 78]
]

print("Students:", students)
print("First student:", students[0])
print("Sachin's marks:", students[0][1])


print("\n" + "-" * 45)
print("✅ Python Lists Practice Completed!")