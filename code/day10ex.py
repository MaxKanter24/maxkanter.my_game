# file created by Max Kanter
# file from Chris Cozort 

# libraries
from time import sleep
# random pseudo random
from random import randint

playing = True
choices = ["rock","paper","scissors"]

# print("Let's play: " + str(choices))
print("Let's play: ", choices[0], choices[1], choices[2])

def get_userchoice():
    global user_choice
    user_choice = input("Choose rock paper or scissors...")

def cpu_choice():
    return choices[randint(0,2)]

# def wanna_play():
#     response = input("do you want to play rock paper scissors?")
#     if response == "no":
#         return False
#     elif response == "yes":
#         print("attaboy!!!")
#         return True
#     else:
#         print("need more input....")
# game, catdog, battle, start, rock_paper_scissors
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
        print("An error of type 0affedf0")

# while True:
#     playing = wanna_play()
#     print("playing is", playing)
#     if playing == False:
#         break
#     else:
#         get_userchoice()
#         compare()
rps()

 