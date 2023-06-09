# file created by Max Kanter
# Absent 3/6
# Code from Chris Cozort

import pygame as pg

from pygame.sprite import Sprite

from settings import *

vec = pg.math.Vector2

# player class

class Mob(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.width = WIDTH
        self.height = HEIGHT 
        self.image = pg.Surface((self.width,self.height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        # self.canjump = False
    def input(self):
        keystate = pg.key.get_pressed()

        if keystate[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        elif keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        elif keystate[pg.K_s]:
            self.acc.y = PLAYER_ACC
        elif keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
# this will keep it on screen via barrier
# pacman effect
    def inbound(self):
        if self.rect.x > WIDTH:
            self.pos.x = 0
        if self.rect.y > HEIGHT:
            self.pos.y = 200
        if self.rect.x < 0:
    # self is any instance of player
    def behavior(self):
        print(self.vel)
        self.acc.y = -2
       
    def update(self):
        self.inbound()
        self.acc = self.vel * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos

