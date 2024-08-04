# def cube(x):
#     return x*x*x

l=[]
n = int(input("Value of n :\n"))

for i in range (n+1):
    l.append(i)
    

newl = list(map(lambda x: x*x*x,l))

print(newl)