def repchar(str1):
    
    ch1 = str1[0]
    for i in range(1,len(str1)):
        if str1[0] == str1[i]:
            i += 1
        else:
            ch2 = str1[i]
            
    for j in range(str1):
        if str1[i] == ch1:
            ch1 = ch2
        else :
            str1[i] == ch2
            ch2= ch1    
            
str1 = "raghav"
print(repchar(str1))