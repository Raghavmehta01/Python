def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]== target:
            return i
    else:return -1
    
arr = [1,4,77,5,7]    
print(linearSearch(arr,7))