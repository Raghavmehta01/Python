class animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
        
    def drink(self):
        print(f"{self.name} drinks water")
        
        
        
class dog(animal):
    def __init__(self,name,breed):
         super().__init__(name)
         self.breed = breed
        
    def bark(self):
        print(f"{self.name} which is of {self.breed} breed barks ")
    
    
class kangaroo(animal):
    def __init__(self,name,region):
        super().__init__(name) 
        self.region = region
        
    def jump(self):
        print(f"{self.name} which is a kangaroo of region {self.region} jumps")
        
        
o = dog("tommy","german sheaphard")
o.bark()

m = kangaroo("Drooper","Australian")
m.jump()