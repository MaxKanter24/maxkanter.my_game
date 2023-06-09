#file created by Max KAnter
import pygame as pg

from pygame.sprite import Sprite

from settings import *

vec = pg.math.Vector2

from random import randint

import time


# player class

seconds = time.time()
print()

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
        self.standing = False
    
    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
    # ...
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP
    # def inbounds(self):
    #     if self.rect.x > WIDTH - 50:
    #         self.pos.x = WIDTH - 25
    #         self.vel.x = 0
    #         print("i am off the right side of the screen...")
    #     if self.rect.x > 0:
    #         self.pos.x = 25
    #         self.vel.x = 0
    #         print("i am off the left side of the screen...")
    #     if self.rect.y > HEIGHT:
    #         print("i am off the bottom of the screen")
    #     if self.rect.y < 0:
    #         print("i am off the top of the screen...")
    def mob_collide(self):
            hits = pg.sprite.spritecollide(self, self.game.enemies, False)
                
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)  
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos
        
#trying to get two different classes of mobs, different mobs make different score
class Mob(Sprite):
    def __init__(self,width,height, color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = GREEN
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/6, HEIGHT/4)
        self.pos = vec(WIDTH/10, HEIGHT/6)
        self.vel = vec(randint(1,3),randint(1,3))
        self.acc = vec(1,1)    
# class Mob(Sprite):
#     def __innit__(self,width,height, color):
#         self.width = width
#         self.height = height
#         self.image = pg.Surface((self.width,self.height))
#         self.color = RED
#         self.image.fill(self.color)
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH/1, HEIGHT/3)
#         self.pos = vec(WIDTH/5, HEIGHT/5)
#         self.vel = vec(randint(1,4),randint(2,2))
#         self.acc = vec(1,2)

    # ...
    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.x < 0:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y < 0:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
    def update(self):
        self.inbounds()
        # self.pos.x += self.vel.x
        # self.pos.y += self.vel.y
        self.pos += self.vel
        self.rect.center = self.pos

# create a new platform class...

class Platform(Sprite):
    def __init__(self, width, height, x, y, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant
       