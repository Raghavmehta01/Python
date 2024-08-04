class Student:
    def __init__(self,name,Class):
        
        self.name = name
        self.Class = Class
        
        if len(name) > 6:
            def change() :
                print("Not accepted")
                

class teacher(Student):
    def location(self,location):
        self.location = location
        
        print(f"Name and class : {self.name} and {self.Class}")
        print("and Location is {self.location}")
        
n1 = teacher('raghav',21)
n1.location('indore')
        