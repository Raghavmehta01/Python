import random


options = ("rock","paper",'scissors')
computer = random.choice(options)
player = None


player = int(input("Enter one of three options:\n 0 for Rock\n 1 for Paper\n 2 for Scissor \n"))

0,1,2

if(player==computer):
    print("tie")
elif(player<computer):
    print("Player wins")
else:
    print("computer wins")

    