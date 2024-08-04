def Anagrams(str1,str2):
    if sorted(str1) == sorted(str2):
        print("Anagram")
    elif sorted(str1.lower()) == sorted(str2.lower()):
        print("CAnagram")
    
    else:
        print("Not Anagrams")
        
str1 = "raGhav"
str2 = "ahgrav"        
Anagrams(str1,str2)