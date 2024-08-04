def anagrams(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
    
    
str1 = input("Enter first word :  ")
str2 = input("Enter second word:  ")
print(anagrams(str1,str2))

