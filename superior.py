arr = []
n = int(input("Number: "))
for i in range(n):
    num = int(input("Enter elemnt: "))
    arr.append(num)
    
count = 0
value = n-1

for j in range(n-2,-1,-1):
    if arr[j] > value:
        count += 1
    
    
print(count)