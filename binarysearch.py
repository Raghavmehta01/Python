def binarysearch(arr,target):
    start = 0
    end = len(arr) -1
    mid = (start + end)//2
    
    if mid == target:
        print(arr[mid])
    elif mid > target:
        start = mid +1
    else:
        end = mid-1
        
    return -1


arr = [1,23,45,8,9,7]
print(binarysearch(arr,7))