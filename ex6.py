# making stone , paper , scissor game using python

import random
print("Welcome to the game\n")
def game():
    print("what you want to choose (stone , paper or scissor\n")
    user=input("enter here")
    lst=["stone", "paper" , "scissor"]
    cpu=random.choice(lst)

    if user=="stone" and cpu=="stone":
        print("cpu choose stone\n")
        print("match tied")
    elif user=="stone" and cpu=="paper":
        print("cpu choose paper\n")
        print("you loose!")
    elif user=="stone" and cpu=="scissor" :
        print("cpu choose scissor\n")
        print("you won ")

    if user=="paper" and cpu=="stone":
        print("cpu choose stone\n")
        print("you loose!")
    elif user=="paper" and cpu=="paper":
        print("cpu choose paper\n")
        print("game tied!")
    elif user=="paper" and cpu=="scissor" :
        print("cpu choose scissor\n")
        print("you won ")

    if user=="scissor" and cpu=="stone":
        print("cpu choose stone\n")
        print("you loose!")
    elif user=="scissor" and cpu=="paper":
        print("cpu choose paper\n")
        print("you won")
    elif user=="scissor" and cpu=="scissor" :
        print("cpu choose scissor\n")
        print("game tied ")

    else:
        return "invalid"
game()
game()
game()
game() #how many times you want to play we set 5 times
game()
print("thanks for playing the game")