def choice(a,b,c):
    if 0<c<=4:
        if c==1:
            return a+b
        elif c==2:
            return a-b
        elif c==3:
            a*b
        else:
            a/b
            
    else:
        print("Invalid input")
        
a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))

print(choice(a,b,c))