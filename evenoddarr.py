A =[]

N = int(input("Enter size of arr: "))

for i in range(N):
    Arr =   int(input("Enter values:") )
    A.append(Arr)
    
    
# A= [1,4,5,67,7]
Even =[]
odd = []
for i in range(N+1):
    if (i%2==0):
        Even.append(i)
    else:
        odd.append(i)
        
Final =[Even + odd]
print(Final)


        

        
        