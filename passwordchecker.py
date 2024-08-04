def CheckPassword(n,length):
    
    
    iscap = 0
    isnum = 0
    
    
    if (length < 4):
        return 0
    if n[0].isdigit():
        return 0
    
    for i in range(length):
        if n[i].isdigit():
            isnum = isnum +1
        if n[i].isupper():
            iscap = iscap + 1
        elif n[i] == ' ' or n[i] == '/'  :
            return 0
        
    if iscap > 0 and isnum > 0:
        return 1
    else:
        return 0
    

n = input("Enter Password : ")
length = len(n)    
CheckPassword(n,length)

if CheckPassword(n, length) == 1:
    print("Password fine")
else:
    print("Recheck password")