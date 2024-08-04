class Raghav:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
        print(f"Name : {self.name} and age : {self.age}")
        
    # def show(self):
    #     print(f"Name and Age of employee is : {self.name} and {self.age}")
        
        
    
        
class Mehta(Raghav):
    def Location(self,location):
        self.location = location
        print(f"Location is {self.location}")
        
        

n2 = Mehta("raghav",21)
n2.Location("indore")



# n1 = Raghav("Raghav" , 21)
# n1.show()