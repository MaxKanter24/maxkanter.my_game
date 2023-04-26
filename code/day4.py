# File created by Max Kanter
'''
File created by:  Chris  Cozort

This series of files will include a step by step process for creating a basic pygame-based game in python

RESOURCE: https://www.w3schools.com/python/default.asp 

On installing pygame: 
Pygame isn't updated for python 3.11, but you 
can still install a pre-version with pip install pygame --pre

Scavenger hunt: Comment on the following items as you see them below:
- Variables- contains infromation storing data values 
- Data Types
- Numbers- One of three different number types int, float, complex
- Strings- Text that is surrounded by quotation marks, single or double quote marks are equal
- Booleans- An expression giving one of two answers: true or false
- Operators- Math related numeric values to preform common mathematical functions ex. +, -, *, /
- Tuples- Multiple items stored in one line, divided by commas 
- While loops- 2 different loop commands, while, for, will execute command if statment is true
- For loops- The for loop repeats statements
- If Else Conditional statements
- Functions- Defenition of a word 
****BONUS****
- Classes
'''
# 
import pygame as pg

from pygame.sprite import Sprite

from random import *

from math import *

import os


vec = pg.math.Vector2

"""
From https://www.geeksforgeeks.org/__file__-a-special-variable-in-python/ 
A double underscore variable in Python is usually referred to as a dunder. A dunder variable is a 
variable that Python has defined so that it can use it in a “Special way”. 
This Special way depends on the variable that is being used.
The variable below __file__ is a variable that contains the path to the module that is currently being imported.
"""
# file for game 
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
# Bool will decide whether true and false
print("here's the current game folder", game_folder)
print("here's the current game folder", img_folder)
# Variable that declares the width of the game screen
WIDTH = 800
# Variable or number that decalres the height of the game screen
HEIGHT = 600
# Variable delcares amount of frames recived per second on game screen. 
FPS = 30
# tuple that creates an RGB value that pygame uses
# tuple is variable 
# (0,0,0) is a tuple, repating duplicate items
BLACK = (0,0,0)
# 
WHITE = (255,255,255)
TILESIZE = 64
#   
x = 0
y = 0

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
# string 
pg.display.set_caption("My First Pygame...")
clock = pg.time.Clock()

# boolean value that determines if the game is running
running = True
# rate that the white tile moves across screeen display
speed = 5

while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:

            running = False
    
    ##### UPDATE #####
    x += speed * FPS/1000
    # y += speed * FPS/1000
    rect = pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
    
    #####  DRAW  #####
    screen.fill(BLACK)
    pg.draw.rect(screen, WHITE, rect)

    pg.display.flip()

pg.quit()