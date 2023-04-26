# file created by Max Kanter
# file from Chris Cozort 

# libraries
from time import sleep
# random pseudo random
from random import randint

playing = True
choices = ["rock","paper","scissors"]

# prints lets play and 3 options
print("You must play this game with me, we shall duel in the art of: ", choices[0], choices[1], choices[2])

def get_userchoice():
    global user_choice
    user_choice = input("Choose rock paper or scissors...")
#cpu random choice
def cpu_choice():
    return choices[randint(0,2)]


def rps():
    get_userchoice()
    cpu = cpu_choice()
    print("The computer chose", cpu)
    if user_choice == cpu:
        print("Tie!!")
    elif user_choice == "rock":
        if cpu == "scissors":
            print("You win!")
        elif cpu == "paper":
            print("You lose!")
    else:
        print("HEHH??")


rps()

 



