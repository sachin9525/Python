# ==========================================
# Behind the Scenes of Loops in Python
# ==========================================

print("🐍 PYTHON LOOP INTERNALS")
print("-" * 45)


# ==========================================
# 1. Iterable Object
# ==========================================

print("\n1. Iterable Object")

numbers = [10, 20, 30, 40]

print("List:", numbers)
print("Type:", type(numbers))


# ==========================================
# 2. Creating Iterator using iter()
# ==========================================

print("\n2. Creating Iterator")

iterator = iter(numbers)

print("Iterator:", iterator)
print("Iterator Type:", type(iterator))


# ==========================================
# 3. Getting Values using next()
# ==========================================

print("\n3. Using next()")

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# ==========================================
# 4. StopIteration
# ==========================================

print("\n4. Handling StopIteration")

iterator = iter([1, 2, 3])

while True:

    try:
        value = next(iterator)
        print("Value:", value)

    except StopIteration:
        print("Iteration Completed!")
        break


# ==========================================
# 5. How for Loop Works Internally
# ==========================================

print("\n5. For Loop")

languages = ["Python", "JavaScript", "Java"]

for language in languages:
    print(language)


# ==========================================
# 6. Same For Loop Manually
# ==========================================

print("\n6. For Loop Internal Working")

languages = ["Python", "JavaScript", "Java"]

iterator = iter(languages)

while True:

    try:
        language = next(iterator)
        print(language)

    except StopIteration:
        break


# ==========================================
# 7. Iterator with String
# ==========================================

print("\n7. String Iterator")

language = "Python"

iterator = iter(language)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# ==========================================
# 8. Iterator with Tuple
# ==========================================

print("\n8. Tuple Iterator")

skills = ("Python", "React", "Node.js")

iterator = iter(skills)

while True:

    try:
        print(next(iterator))

    except StopIteration:
        break


# ==========================================
# 9. Check Iterable vs Iterator
# ==========================================

print("\n9. Iterable vs Iterator")

numbers = [1, 2, 3]

iterator = iter(numbers)

print("List has __iter__:", hasattr(numbers, "__iter__"))
print("List has __next__:", hasattr(numbers, "__next__"))

print(
    "Iterator has __iter__:",
    hasattr(iterator, "__iter__")
)

print(
    "Iterator has __next__:",
    hasattr(iterator, "__next__")
)


# ==========================================
# 10. Custom Iterator
# ==========================================

print("\n10. Custom Iterator")


class NumberIterator:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


numbers = NumberIterator(1, 5)

for number in numbers:
    print(number)


# ==========================================
# 11. range() is Iterable
# ==========================================

print("\n11. range() Iterator")

numbers = range(1, 6)

iterator = iter(numbers)

while True:

    try:
        print(next(iterator))

    except StopIteration:
        break


# ==========================================
# 12. Important Demonstration
# ==========================================

print("\n12. Iterator Remembers Its Position")

numbers = [100, 200, 300]

iterator = iter(numbers)

print("First:", next(iterator))
print("Second:", next(iterator))
print("Third:", next(iterator))

try:
    print(next(iterator))

except StopIteration:
    print("No more values available!")


# ==========================================
# Completed
# ==========================================

print("\n" + "-" * 45)
print("✅ Python Loop Internals Practice Completed!")