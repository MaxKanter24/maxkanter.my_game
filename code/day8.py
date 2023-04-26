# This file was created by Max Kanter


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
# pauses printing lines
from time import sleep 
# imputs random value given and pastes in terminal
from random import randint

# choices = [0,1,2]
choices0 = ["rock", "paper", "scissors"]
choices1 = ["Rizzard", "Theif", "Fighter" ]
games = [choices0, choices1]
# prints whats choices in games 0 or 1 
print(games)
# prints choiecs0
print(games[0])
# prints first game and first option in choice0
print(games[0][0])
# prints first option in games, first option in str, first value of first option
print(games[1][2][0])
# print will not work because it is out of the range 
# print(games[0][0][0][10])

# takes a 10 second rest before printing all
# sleep(10)

# print("Lets play:" + str(choices))
print("Lets Play: ")
# print options for Rock, Paper or Scisscors in the terminal
# prints the first option from choices0
print(choices0 [0])
# prints second option from choices0
print(choices0 [1])
#prints last option from choices0
print(choices0 [2])

catdog = 9 
for catdog in choices0:
    print(catdog)
    # pause for 3 seconds
# sleep(3)
print(catdog)

# range: function returns a sequence of numbers and stops before a speceficied number
#  len tells how many integers
for i in range(len(choices0)):
    print("this is index" + str(i))
    # j is a alternate value swapped with i
    j = choices0[j]
    print("This is the value in the list" + j)

# print("Lets play rock paper scissors")

# User types choice into terminal
user_choice = input("Choose rock paper or scisscors: ")
# prints option to pick a variable in terminal 
print("You chose: " + user_choice)
# let computer pick a random option 0,1,2

def cpu_choice():
    # after you chose, computer prints in terminal along with cpu choice
    return  choices0[randint(0,2)]
    # return "The computer has chosen something..." +choices0[randint(0,2)]

# print(choices[randint(0,2)])
print(cpu_choice())


y = 5
x = 6
def compare(x,y):
    if x== y:
        print("samesies")
        # if not true
    else:
        print: ("not samesies")
    if x == "rock" and y == "scissors":
        print(DUB!!!!)

compare("rock", "scisscors")
compare(user_choice, "scisscors")