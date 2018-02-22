import pygame, sys
from pygame.locals import *
import random
from random import randint
import time
from time import sleep
# set up pygame
pygame.init()
pix_siz = 10
grid_x = 32
grid_y = 32

width = pix_siz*grid_x
height = pix_siz*grid_y

windowSurface = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Snake Game')

BLACK = (50,50,50,255)
WHITE  = (255,255,255,255)
RED = (255,200,200,255)
GREEN = (0,255,0,255)

class snake():
    def __init__(self,pos_x,pos_y,dire,t_size):
        self.x = pos_x
        self.y = pos_y
        self.d = dire
        self.tail = []
        self.f = 0
        for i in range(t_size):
            self.tail.append([self.x - i*pix_siz,self.y])
    def update(self):

        if self.d == 1:
            self.x+= pix_siz
        if self.d == 2:
            self.y+=pix_siz
        if self.d == 3:
            self.x-= pix_siz
        if self.d == 0:
            self.y-= pix_siz
        if self.x > width-1:
            self.x = 0
        if self.x <0:
            self.x = width-1-pix_siz
        if self.y <0:
            self.y = height-1-pix_siz
        if self.y > height-1:
            self.y = 0
        if windowSurface.get_at((self.x,self.y)) == GREEN:
            for i in food_l:
                if abs(self.x-i.x+1)<=5 and abs(self.y-i.y+1)<=5:
                    i.move()
                    self.f += 2


        if windowSurface.get_at((self.x,self.y)) ==WHITE:
            self.x =399
            self.y = 399
            self.d= 0
            self.tail = []
            self.f = 0
            for i in range(3):
                self.tail.append([self.x - i*pix_siz,self.y])

        if self.f ==0:

            self.tail.insert(0,[self.x,self.y])
            self.tail.pop(len(self.tail)-1)
        else:

            self.tail.insert(0,[self.x,self.y])
            print len(self.tail)
            self.f-=1
    def represent(self):
        pygame.draw.rect(windowSurface,RED,(self.tail[0][0],self.tail[0][1],pix_siz,pix_siz))
        for i in self.tail[1:]:
            pygame.draw.rect(windowSurface,WHITE,(i[0],i[1],pix_siz,pix_siz))
s = snake(399,399,1,3)

class food():
    def __init__(self,pos_x,pos_y):
        self.x = pos_x
        self.y = pos_y
    def represent(self):
        pygame.draw.rect(windowSurface,GREEN,(self.x,self.y,pix_siz*1,pix_siz*1))
    def move(self):
        self.x = randint(1,grid_x-2)*pix_siz
        self.y = randint(1,grid_y-2)*pix_siz
        if windowSurface.get_at((self.x,self.y)) ==WHITE:
            self.move()
t = time.clock()
food_l = []
f_q =2
for i in range(f_q):
    food_l.append(food(randint(1,grid_x-2)*pix_siz,randint(1,grid_y-2)*pix_siz))
des_d = s.d
while True:

    act_ti = 0.11
    if time.clock()-t > act_ti:
        s.d = des_d
        windowSurface.fill(BLACK)
        for i in food_l:
            i.represent()
        s.represent()
        s.update()
        pygame.display.update()
        t = time.clock()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys=pygame.key.get_pressed()
    if keys[K_LEFT]:
        if s.d != 1:
            des_d = 3
    if keys[K_DOWN]:
        if s.d != 0:
            des_d = 2
    if keys[K_RIGHT]:
        if s.d != 3:
            des_d = 1
    if keys[K_UP]:
        if s.d !=2:
            des_d = 0
