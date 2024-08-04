def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            
        else:
            i=i+1
            
print(isPrime(4))
            
            