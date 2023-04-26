# File created by: Max Kanter 

'''
Step by Step Process for playing Rock Paper Scisscors
1. Find and aggre with opponenct regarding rules (amount of games, shoot or not)
2. Intense staring contest (To read their mind)
3. Both say the words "Rock, Paper, Scisscors (shoot optional) takes about 3 seconds
4. Pick either Rock, Paper or Scisscors 
5. Win or loose or tie
6. 
Algorthims- step by step proccess

Goals: Win
Rules: Pick Rock, Paper or Scisscors at the same time opponent does
Feedback: Winning, Losing, or tie with opponent.
Freedom: Can pick any of the 3 options, play desired amount of rounds

Nouns and Verbs in RPS
variables and function
Nouns- rock, paper, scisccors, hands, points, opponent, input
Verbs- win, loose, tying, comparing outcomes, deciding, shoot, challenging

r>p>s>r


'''

# libraries
from time import sleep 
from random import randint

# choices = [0,1,2]
choices = ["rock", "paper", "scissors"]

# print("Lets play:" + str(choices))
print("Lets Play: ")
# print options for Rock, Paper or Scisscors in the terminal
print(choices [0])
print(choices [1])
print(choices [2])
# pause for 3 seconds
sleep(3)

# print("Lets play rock paper scissors")

# User types choice into terminal
user_choice = input("Choose rock paper or scisscors")
# prints option to pick a variable in terminal 
print("You chose" + user_choice)
# let computer pick a random option 0,1,2
def cpu_choice():
    # after you chose, computer prints in terminal along with cpu choice
    return "The computer has chosen something..." +choices[randint(0,2)]

# print(choices[randint(0,2)])
print(cpu_choice())