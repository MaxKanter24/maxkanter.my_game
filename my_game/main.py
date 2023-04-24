# file created by Max Kanter
# absent 3/6
# Code from Chris Cozort
#w3 schools and other sites used

# File created by: Chris Cozort
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed something - I changed something else tooooo!

# This file was created by: Chris Cozort
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
'''


'''
# import libs
import pygame as pg
import random
import os
# import settings 
from settings import *
from sprites import *
import time
# from pg.sprite import aSprite
# set up assets folders

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")



# create game class in order to pass properties to the sprites file 
class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.score = 0
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.plat1 = Platform(WIDTH, 70, 0, HEIGHT-50, (150,150,150), "icey")
        self.plat2 = Platform(100, 15, 50, 450, WHITE ,"bouncey")
        self.plat3 = Platform(100, 15, 500, 200, WHITE ,"bouncey")
        self.plat4 = Platform(100, 15, 250, 320, WHITE ,"bouncey")
        self.all_sprites.add(self.plat1)
        self.platforms.add(self.plat1)
        self.platforms.add(self.plat2)
        self.platforms.add(self.plat3)
        self.platforms.add(self.plat4)
        self.all_sprites.add(self.plat2)
        self.all_sprites.add(self.plat3)
        self.all_sprites.add(self.plat4)
        self.all_sprites.add(self.player)
        # the score willa add up t0 second number every time(50)
        for i in range(0,9):
            m = Mob(24,20,(0,255,0))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                for platform in hits:
                    self.player.standing = True
                    if hits[0].variant == "normal":
                        self.player.vel.y = 0
                    elif hits[0].variant == "icey":
                        self.player.pos.y = hits[0].rect.top
                        self.player.vel.y = 0
                        PLAYER_FRICTION = 0
                    elif hits[0].variant == "bouncey":
                        self.player.pos.y = platform.rect.top
                        self.player.vel.y = -PLAYER_JUMP
                    else:
                        self.player.pos.y = platform.rect.top
                        self.player.vel.y = 0
                else:
                    self.player.standing = False
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.playing = True
        enemy_hits = pg.sprite.spritecollide(self.player, self.enemies, True)
        #adds to number score related to the i in range
        self.score += len(enemy_hits)
        if self.score == 9:
            playing = False
         # True will remove the collided enemies from the group
    # Increase score for each enemy hit
       

    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        font = pg.font.Font(None, 36)
        # displays score starting 0
        score_text = font.render("Score: {}".format(self.score), True, WHITE)  
        self.screen.blit(score_text, (10,10))
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            score_text =+ 1
        pg.display.flip()

    # self.draw_text("SCORE", 24, WHITE, WIDTH/2, HEIGHT/8)
       
    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

g = Game()
# kick off the game loop
while g.running:
    g.new()

pg.quit()