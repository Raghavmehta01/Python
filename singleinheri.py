class employee:
    def __init__(self,name):
        self.name = name
        
    def show(self):
        print(f"The name is {self.name}")
        
class dance:
    def __init__(self,dance):
        self.dance = dance
        
    def show(self):
        print(f"The dance is {self.dance}")
        
class danceremp(dance,employee):
    def __init__(self,name,dance):
        self.name = name
        self.dance= dance
        
        print(f"The name is {self.name} and Dance is {self.dance}")
        
        
o = danceremp("Raghav","kathak")
print(danceremp.mro())

# o.show()
