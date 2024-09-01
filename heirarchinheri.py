class Food:
    def __init__(self):
        print("Hello to Food class")
        
class MainCourse(Food):
    def __init__(self, name):
        super().__init__()  # Call the parent class constructor
        self.name = name
        print(f"Welcome to subclass MainCourse and the dish's name is {self.name}")
        
class Dessert(Food):
    def __init__(self, name):
        super().__init__()  # Call the parent class constructor
        self.name = name
        print(f"Welcome to subclass Dessert and the dessert's name is {self.name}")
        
class Paneer(MainCourse):
    def __init__(self, name, paneer_type):
        super().__init__(name)  # Initialize the MainCourse with name
        self.paneer_type = paneer_type
        
    def show(self):
        print(f"This is a child class of subclass MainCourse and the type of paneer that will be served is {self.paneer_type}")
        
# Example usage
o = Paneer("Mutter Paneer", "Spicy")
o.show()

# p = Dessert("Rasmalai")
