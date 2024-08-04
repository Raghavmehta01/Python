def __init__(self,num1,num2,operation):
    self.num1 = num1
    self.num2 = num2
    self.operation = operation
    
    if operation not in ('+','-','*','/'):
        raise ValueError("Enter correct operation")

def calculate(self):
    if self.operation == '+':
        print(f"Sum of {self.num1} and {self.num2} is ")