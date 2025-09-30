dobbel=0
import random
guess=690
while (dobbel!=guess):
    dobbel=random.randrange(1, 6)
    print("1 tot 6, give me your best shot")
    guess=int(input())
    if (guess==dobbel):
        print("you win")
    else:
        if (guess != 1 < 7):
            print ("fuck you")
        else:
            print("you lose, the number was", dobbel)