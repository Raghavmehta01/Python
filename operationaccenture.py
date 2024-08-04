N = int (input())

while N >= 10:
    
    if N%2==0:
        N = (N-2)/2
    print(int(N))
    
    
    N = N/2
    print(int(N))
    
print(N)