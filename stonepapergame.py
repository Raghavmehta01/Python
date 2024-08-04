import random

com = random.randint(0,2)
player = int(input("Enter a number : 0 for Stone, 1 for Paper, 2 for scissor "))
if player < 0 or player > 2 :
    print("Error, Enter between the given range")
else:
    print(f"Value chosen by the user is {player}")
    print(f"Value chosen by the computer is {com}")
def check(com,player):
    
    
    
    if com == player :
        print("tie")
        
    elif player == 0 and com >0 :
        print("com wins")
        
    elif player == 1 and com > 1:
        print("Com wins")
        
    elif player == 2 and com <2:
        print("player wins")
        
check(com,player)
    
    
    
  