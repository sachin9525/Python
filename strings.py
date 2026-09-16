# ==========================================
# Python Strings Practice
# Learning Python - Strings
# ==========================================

print("🐍 PYTHON STRINGS PRACTICE")
print("-" * 40)

# 1. Creating a String
name = "Sachin Kumar"
language = "Python"

print("\n1. Creating Strings")
print("Name:", name)
print("Language:", language)


# 2. String Indexing
text = "Python"

print("\n2. String Indexing")
print("String:", text)
print("First character:", text[0])
print("Second character:", text[1])
print("Last character:", text[-1])


# 3. String Slicing
print("\n3. String Slicing")
print("text[0:3]:", text[0:3])
print("text[2:]:", text[2:])
print("text[:4]:", text[:4])
print("Reverse string:", text[::-1])


# 4. String Concatenation
first_name = "Sachin"
last_name = "Kumar"

full_name = first_name + " " + last_name

print("\n4. String Concatenation")
print("Full Name:", full_name)


# 5. String Length
message = "Learning Python"

print("\n5. String Length")
print("Text:", message)
print("Length:", len(message))


# 6. Uppercase and Lowercase
print("\n6. Changing Case")
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Title Case:", message.title())


# 7. Replace
course = "I am learning JavaScript"

print("\n7. Replace String")
print("Before:", course)

course = course.replace("JavaScript", "Python")

print("After :", course)


# 8. Find
sentence = "Python is easy and powerful"

print("\n8. Find in String")
print("Sentence:", sentence)
print("Position of 'easy':", sentence.find("easy"))
print("Position of 'Python':", sentence.find("Python"))


# 9. Split
technologies = "Python,React,Node,MongoDB"

print("\n9. Split String")
tech_list = technologies.split(",")

print("Original:", technologies)
print("After Split:", tech_list)


# 10. Join
skills = ["Python", "React", "Node.js"]

print("\n10. Join Strings")
result = " | ".join(skills)

print("Skills:", result)


# 11. f-Strings
name = "Sachin"
skill = "Python"

print("\n11. f-String")
print(f"My name is {name} and I am learning {skill}.")


# 12. Escape Characters
print("\n12. Escape Characters")
print("Python\nProgramming")
print("Python\tDeveloper")
print('I\'m learning Python')


# 13. Checking String Content
word = "Python123"

print("\n13. String Checking")
print("Is alphabetic:", word.isalpha())
print("Is numeric:", word.isnumeric())
print("Is alphanumeric:", word.isalnum())


# 14. Remove Spaces
username = "   Sachin Kumar   "

print("\n14. Strip Spaces")
print("Before:", repr(username))
print("After :", repr(username.strip()))


# 15. String Immutability
print("\n15. String Immutability")

language = "Python"

print("Original:", language)

# language[0] = "J"
# The above line gives TypeError because strings are immutable.

language = "J" + language[1:]

print("New String:", language)


# 16. Small Practice - Reverse a String
text = "Python"

reversed_text = text[::-1]

print("\n16. Reverse String")
print("Original:", text)
print("Reversed:", reversed_text)


# 17. Small Practice - Count Characters
text = "programming"

print("\n17. Character Count")
print("Text:", text)
print("Count of 'm':", text.count("m"))


# 18. Small Practice - Check Word
sentence = "I am learning Python"

print("\n18. Membership Check")
print("Python" in sentence)
print("Java" in sentence)


print("\n" + "-" * 40)
print("✅ Python Strings Practice Completed!")