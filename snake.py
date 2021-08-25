import pygame
SIZE=40
class Snake:
    def __init__(self,parent_screen,length):
        self.parent_screen=parent_screen
        self.block=pygame.image.load("resources/block.jpg").convert()    #used to load image from folder and convert() is used to create a copy that will draw more quickly on the screen
        self.length=length
        self.x=[120]*length
        self.y=[120]*length
        self.direction='up'         #representing initial direction is down
    def draw(self):
        for i in range(0,self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()

    def move_up(self):
        self.direction='up'
        
    def move_down(self):
        self.direction='down'
        
    def move_right(self):
        self.direction='right'
        
    def move_left(self):
        self.direction='left'
        
    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]
        if self.direction=='left':
            self.x[0]-=SIZE
        elif self.direction=='right':
            self.x[0]+=SIZE
        elif self.direction=='up':
            self.y[0]-=SIZE
        elif self.direction=='down':
            self.y[0]+=SIZE
        self.draw()