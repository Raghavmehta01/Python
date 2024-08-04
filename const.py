# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # # Accessing attributes
# print(person1.name)  # Output: Alice
# print(person1.age)   # Output: 30


# # Creating an instance of the Person class
# person1 = Person("Alice", 30)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person {self.name} is created.")

    def __del__(self):
        print(f"Person {self.name} is destroyed.")

# Creating an instance of the Person class
person1 = Person("Alice", 30)

# The __del__ method is called when the object is about to be destroyed
del person1
