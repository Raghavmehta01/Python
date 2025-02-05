
def counter(w):
    tw = 0 
    fw = 0
    if w % 2 == 0:
       
        
        fw =w // 4 
        new_2 = w - (fw*4) 
        tw += new_2//2   
    
        return f"Number of Four wheelers = {fw}\nNumber of Two wheelers = {tw}"
    else:
        return "Invalid input: Total wheels must be an even number."
        
w = int(input("Number of wheels : "))
print(counter(w))
        