import pygame, sys
from pygame.locals import *
import random
from random import randint
import time
from time import sleep
# set up pygame
pygame.init()
pix_siz = 10
grid_x = 16
grid_y = 16
grid = []

width = pix_siz*grid_x
height = pix_siz*grid_y

windowSurface = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Snake Game')

BLACK = (125,125,125,255)
WHITE  = (255,255,255,255)
RED = (255,50,50,255)
GREEN = (0,255,0,255)
BLUE = (50,50,255,255)
for i in range(grid_y):
    grid.append([])
for i in grid:
    for l in range(grid_x):
        i.append(BLACK)
class snake():
    def __init__(self,pos_x,pos_y,dire,t_size,color):
        self.x = pos_x
        self.y = pos_y
        self.d = dire
        self.tail = []
        self.f = 0
        self.c = color
        for i in range(t_size):
            if self.d == 1:
                self.tail.append([self.x - i,self.y])
            if self.d == 2:
                self.tail.append([self.x,self.y-i])
            if self.d == 3:
                self.tail.append([self.x + i,self.y])
            if self.d == 0:
                self.tail.append([self.x,self.y + i])
            
    def update(self):
        if self.d == 1:
            self.x+= 1
        if self.d == 2:
            self.y+=1
        if self.d == 3:
            self.x-= 1
        if self.d == 0:
            self.y-= 1
        if self.x > grid_x-1:
            self.x = 0
        if self.x <0:
            self.x = grid_x-1
        if self.y <0:
            self.y = grid_y-1
        if self.y > grid_y-1:
            self.y = 0
        if grid[self.y][self.x] == GREEN:
            for i in food_l:
                if self.x == i.x and self.y == i.y:
                    i.move()
                    self.f += 2


        if grid[self.y][self.x] ==s.c:
            self.die()
        if grid[self.y][self.x] ==a.c:
            self.die()

        if self.f ==0:

            self.tail.insert(0,[self.x,self.y])
            grid[self.tail[-1][1]][self.tail[-1][0]] = BLACK
            self.tail.pop(len(self.tail)-1)
        else:

            self.tail.insert(0,[self.x,self.y])
            self.f-=1
    def represent(self):
        grid[self.y][self.x] = RED
        for i in self.tail[1:]:
            grid[i[1]][i[0]] = self.c
    def die(self):
        for i in self.tail:
            grid[i[1]][i[0]] = BLACK
        self.x =grid_x//2
        self.y = grid_y//2
        self.d= 0
        self.tail = []
        self.f = 0
        for i in range(t_size):
            if self.d == 1:
                self.tail.append([self.x - i,self.y])
            if self.d == 2:
                self.tail.append([self.x,self.y-i])
            if self.d == 3:
                self.tail.append([self.x + i,self.y])
            if self.d == 0:
                self.tail.append([self.x,self.y + i])
s = snake(grid_x//3,grid_y//2,2,3,WHITE)
a = snake(2*grid_x//3,grid_y//2,0,3,BLUE)

class food():
    def __init__(self,pos_x,pos_y):
        self.x = pos_x
        self.y = pos_y
    def represent(self):
        grid[self.y][self.x] = GREEN
    def move(self):
        self.x = randint(1,grid_x-2)
        self.y = randint(1,grid_y-2)
        if grid[self.y][self.x] == s.c:
            self.move()
t = time.clock()
food_l = []
f_q =2
for i in range(f_q):
    food_l.append(food(randint(1,grid_x-2),randint(1,grid_y-2)))
des_d = s.d
desa_d = a.d
while True:
    act_ti = 0.15
    if time.clock()-t > act_ti:
        s.d = des_d
        s.update()
        a.d = desa_d
        a.update()
        windowSurface.fill(BLACK)
        for i in food_l:
            i.represent()
        s.represent()
        for i in range(grid_y):
            for l in range(grid_x):

                pygame.draw.rect(windowSurface,grid[i][l],(l*pix_siz+1,i*pix_siz+1,pix_siz-1,pix_siz-1))
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
    if keys[K_a]:
        if a.d != 1:
            desa_d = 3
    if keys[K_s]:
        if a.d != 0:
            desa_d = 2
    if keys[K_d]:
        if a.d != 3:
            desa_d = 1
    if keys[K_w]:
        if a.d != 2:
            desa_d = 0
