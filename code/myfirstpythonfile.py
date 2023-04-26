#print is a built in python function that prints a text string argument in the terminal
print("Hello there...")
# Turtle is a module that pulls up a drawing window
from turtle import *
# It uses colors red and yellow
color('blue', 'black')
# Begins drawing in window
begin_fill()
# Gives order for drawing cordinates
while True:
    # Moves arrow forward 200 pixels
    forward(200)
    # Arrow moves 170 pixels to the left
    left(200)
    # Absolute value, stop drawing at the line meets at end
    if abs(pos()) < 1:
    # The break tells program to stop drawing
        break
    # Fill in with final color
end_fill()
# Done  
done()