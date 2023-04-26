# file created by max kanter
''''
IPOS: Input, process, output, (store) 

To install pygame on 3.11
'''
# print is a built in function; displays words inbetween parenthesis
# hello there is a string
# hello there is a string argument
# print("Hello, there")
#varaiable, string value

import pygame as pg

Width = 800
Height = 600 
vec = pg.math.Vector2

#init pygame and crate a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...)
clock = pg.time.Clock()

greeting = "Hello there..."


x = True 
y = False 


print(greeting) 
#
# storing a valuee that is returned from the imput function that you type in the terminal
user_input = input("please enter your name: ")
# prints original greeting followed by users input
print(greeting + user_input)