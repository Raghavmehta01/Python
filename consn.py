class Student:
    def __init__(self,Name,class_name) :
        self.name= Name
        self.class_name = class_name
       
        
details = lambda student:  print(f"Name : {student.name}\nClass : {student.class_name}")
   
        

a = input("Enter Name: ")
b = input("Enter class: ")
student1 = Student(a,b)

details(student1)


        
        