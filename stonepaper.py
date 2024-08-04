import random

def choice(Choice):
    user = input("Enter choice between (Stone,Paper,Scissor) " ).lower()
    if user not in ['stone','paper','scissor']:
        print("Invalid input")
    else:
        return user
    
def computer():
    return random.choice(['stone','paper','scissor'])


def winner():
    if user == winner