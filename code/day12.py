# file created by Max Kanter

# import from libraries

from time import sleep
from random import randint 
import pygame as pg 
import os

# setup asset folders - images and sounds as needed
# directory name is afunction that finds file location
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 500
HEIGHT = 500
FPS = 30

#define colors
#tuple ()
# RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

choices = ["Rock,", "Paper", "Scissors"]

def cpu_randchoice():
    choice = choices[randint(0,2)]
    print("computer randomly decides..." + choice)
    return choice
    
pg.init()
pg.mixer.init()
# sets demensions for pop up scereen and caption
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock Paper Scissors")
clock = pg.time.Clock()

#loads images for rps
rock_image = pg.image.load(os.path.join(game_folder, "rock.jpg")).convert()
paper_image = pg.image.load(os.path.join(game_folder, "paper.jpg")).convert()
scissors_image = pg.image.load(os.path.join(game_folder, "scissors.jpg")).convert()
# creates transparency

rock_image.set_colorkey(WHITE)
paper_image.set_colorkey(WHITE)
scissors_image.set_colorkey(WHITE)

rock_rect = rock_image.get_rect()
paper_rect = paper_image.get_rect()
scissors_rect = scissors_image.get_rect()
paper_rect.y = HEIGHT/2
scissors_rect.x = WIDTH/2

cpu_choice = ""
player_choice = ""
###################################################################

running = True
while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
# when hit mousebutton up...
        if event.type == pg.MOUSEBUTTONUP:
# mouse coords= geting mouse coordsrock_image
            mouse_coords = pg.mouse.get_pos()
            # print(mouse_coords)
            # print(mouse_coords[0])
            # print(mouse_coords[1])
            #tuple
            #if click on image of the rock, print
            if rock_rect.collidepoint(mouse_coords):
                print("you clicked DWAYNE")
                player_choice = "Rock"
                cpu_choice = choice()
                # print("u lost")
            elif paper_rect.collidepoint(mouse_coords):
                print("you clicked on DWIGHT")
                player_choice = "Paper"
                # print("L again lol")
            elif scissors_rect.collidepoint(mouse_coords):
                print("you clicked on SCISSORS")
                player_choice = "Scissors"
                # print("L once more hahahah")
            else:
                print("you clicked on nothing")
    
screen.fill(WHITE)
screen.blit(rock_image, rock_rect)
screen.blit(paper_image, paper_rect)
screen.blit(scissors_image, scissors_rect)
    #get memory ready to be used for display at 30 FPS (buffering)
pg.display.flip()
            # print(rock_image.c olliidepoint(mouse_coords))
            # if (rock_image.collidepoint(mouse_coords)):
            # if mouse_coords[0] <= 200 and mouse_coords[1] <= 200:
            # if mouse_coords == pg.mouse.get_pos:
                # print("I clicked on Mr. Johnson")
pg.quit()
            


# get input from player

# update 
# rock_image.x += 1

# draw



