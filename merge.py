def mergeArr(arr1,arr2):
    return arr1 + arr2


arr1= []
arr2 = []

n = int(input("enter size of Array 1 :"))
for i in range(n) :
    temp = int(input("Enter elements : "))
    arr1.append(temp)
    
m = int(input("enter size of Array 2 :"))
for i in range(m) :
    temp =  int(input("Enter elements : "))
    arr2.append(temp)
    
    
print(mergeArr(arr1,arr2))