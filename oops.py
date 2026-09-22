# ==========================================
# Python Object Oriented Programming Practice
# ==========================================

print("🐍 PYTHON OOP PRACTICE")
print("-" * 45)


# 1. Basic Class and Object
print("\n1. Class and Object")

class Student:
    name = "Sachin"
    course = "Python"


student1 = Student()

print("Name:", student1.name)
print("Course:", student1.course)


# 2. Constructor (__init__)
print("\n2. Constructor")

class Developer:
    def __init__(self, name, language):
        self.name = name
        self.language = language


dev1 = Developer("Sachin", "Python")

print("Name:", dev1.name)
print("Language:", dev1.language)


# 3. Instance Method
print("\n3. Instance Method")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)


employee1 = Employee("Sachin", 30000)
employee1.display()


# 4. Multiple Objects
print("\n4. Multiple Objects")

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def details(self):
        print(self.brand, "-", self.price)


laptop1 = Laptop("HP", 55000)
laptop2 = Laptop("Dell", 65000)

laptop1.details()
laptop2.details()


# 5. Class Variable
print("\n5. Class Variable")

class User:
    platform = "Python App"

    def __init__(self, name):
        self.name = name


user1 = User("Sachin")
user2 = User("Rahul")

print(user1.name, "-", user1.platform)
print(user2.name, "-", user2.platform)


# 6. Inheritance
print("\n6. Inheritance")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model S", "85 kWh")

print("Car:", my_tesla.full_name())
print("Battery:", my_tesla.battery_size)


# 7. Method Overriding
print("\n7. Method Overriding")

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says Woof!")


dog = Dog()
dog.sound()


# 8. Encapsulation
print("\n8. Encapsulation")

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount


account = BankAccount(10000)

account.deposit(5000)

print("Balance:", account.get_balance())


# 9. Polymorphism
print("\n9. Polymorphism")

class Cat:
    def sound(self):
        return "Meow"


class Dog:
    def sound(self):
        return "Woof"


animals = [Cat(), Dog()]

for animal in animals:
    print(animal.sound())


# 10. Static Method
print("\n10. Static Method")

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print("Addition:", Calculator.add(10, 20))


# 11. Class Method
print("\n11. Class Method")

class Person:
    species = "Human"

    @classmethod
    def get_species(cls):
        return cls.species


print("Species:", Person.get_species())


# 12. Property Decorator
print("\n12. Property Decorator")

class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Price must be greater than 0")


product = Product(500)

print("Old Price:", product.price)

product.price = 800

print("New Price:", product.price)


# 13. isinstance()
print("\n13. isinstance()")

print(isinstance(my_tesla, ElectricCar))
print(isinstance(my_tesla, Car))


# 14. Multiple Inheritance
print("\n14. Multiple Inheritance")

class Frontend:
    def frontend_skill(self):
        print("Frontend: React")


class Backend:
    def backend_skill(self):
        print("Backend: Python")


class FullStackDeveloper(Frontend, Backend):
    pass


developer = FullStackDeveloper()

developer.frontend_skill()
developer.backend_skill()


# 15. Practical Example
print("\n15. Practical Example")

class DeveloperProfile:

    company = "Tech Company"

    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def show_profile(self):
        print("Name:", self.name)
        print("Skills:", ", ".join(self.skills))
        print("Company:", self.company)

    def add_skill(self, skill):
        self.skills.append(skill)


profile = DeveloperProfile(
    "Sachin Kumar",
    ["Python", "JavaScript", "React", "Node.js"]
)

profile.add_skill("MongoDB")
profile.show_profile()


print("\n" + "-" * 45)
print("✅ PYTHON OOP PRACTICE COMPLETED!")