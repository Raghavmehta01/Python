class Solution:
    def isValid(self, s: str) -> bool:
        round= 0
        curly=0
        square = 0
        for i in s:
            if i == '(' or i == ')':
                round+=1
            elif i == '{' or i ==  '}':
                curly+=1
            elif i == '[' or i == ']':
                square +=1
        if round % 2 == 0 and curly % 2 == 0 and square % 2 == 0:

            return True
        return False
    
    
s = str(input("Enter string"))
new = Solution()
print(new.isValid(s))