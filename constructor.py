class Student:
    def __init__(self):
        self.id = str(input("Enter name:\n"))
        self.role= str(input("Enter role:\n"))
        self.salary= int(input("Enter salary:\n"))
    def display(self):
        print(f"Name: {self.id}")
        print(f"Role: {self.role}")
        print(f"Salry: {self.salary}")

a = Student()        
a.display()