def rat(r,unit,n):
    totalFood = 0
    currentFood = 0
    totalFood= r * unit
    
    if n ==0:
        return -1
    
    for i in range(n):
        currentFood =+ arr[i] 
        if currentFood == totalFood:
            return i +1
    return 0
        
        
r = int(input("Enter rats : "))
unit= int(input("Enter units : "))
n= int(input("Enter size of array : "))
arr = []

for j in range(n):
       arr.append( int(input("Enter values : ")))
print(rat(r,unit,n))