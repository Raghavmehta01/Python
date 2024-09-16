class employee:
    def __init__(self,name):
        self.name = name
        
class dancer:
    def __init__(self,dance):
        self.dance = dance
        
        
class new(employee,dancer):
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name
    # def display(self):
    #     print(self.dance)
    #     print(self.name)
        
input = new("kathak","Raghav")
print(input)

# new.display()