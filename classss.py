class A:
    def getA(self):
        print("base class")
        
class B(A):
    def getB(self):
        self.getA()
        print("Derived")
        

a = B()
a.getB()