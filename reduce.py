from functools import reduce

def mysum(a,b):
    return a+b
num = [1,2,3,4,5,6]

sum = reduce(mysum,num)
print(sum)
