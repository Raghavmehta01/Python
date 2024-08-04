def divSum(n):
    multiple= []
    for i in range(n+1):
        if i%n == 0:
            multiple.append(i)
        else:
            return
        
    for j in multiple:
        next =0
        sum = j +next
        
    return sum


n = 5
print(divSum(n))