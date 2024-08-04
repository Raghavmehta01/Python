n = [input("Enter year : ")]
if n[1] == 0 and n[2] == 0 and n[3] == 0 :
    if n%400==0 :
        print("Leap")
    else:
        print("Not leap")
elif n%4==0:
    print("Leap")
else:
    print("Not leap")