def kgreatest(arr,k):
    unique = list(set(arr))
    unique.sort(reverse=True)
    
    return unique[k]



arr = []
n = int(input("Enter size of array : "))
for i in range(n):
    temp = int(input("Enter elements : "))
    arr.append(temp)
k = int(input("Value of K : "))
print(kgreatest(arr,k))

