class Myclass:
    def __init__(self,value) :
        self._value = value
        
    def show(self):
        print(f"Value is {self._value}")  
    
    @property
    def value(self):
        return 10 * self._value
    
obj = Myclass(10)
obj.show()
print(obj.value)

