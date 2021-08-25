import pygame
SIZE=40
class Apple:
    def __init__(self,parent_screen):
        self.parent_screen=parent_screen
        self.image=pygame.image.load("resources/apple.jpg").convert()
        self.x=SIZE*3
        self.y=SIZE*3

    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()