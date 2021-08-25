import pygame
from pygame.locals import *
import random,time
from snake import Snake
from apple import Apple
SIZE=40
class Game:
    def __init__(self):
        pygame.init()
        self.play_bg_music()
        self.surface= pygame.display.set_mode((1000,600))        #it will create window for game and set window size and return
        self.snake=Snake(self.surface,1)
        self.snake.draw()
        self.apple=Apple(self.surface)
        
    
    def increase_length(self):
        self.snake.length+=1
        self.snake.x.append(-1)
        self.snake.y.append(-1)

    def play_bg_music(self):
        pygame.mixer.music.load("resources/bg_music.mp3")
        pygame.mixer.music.play(-1,0)
        
    def play_sound(self,mp3):
        sound=pygame.mixer.Sound(mp3)
        sound.play()
    def score_display(self):
        font=pygame.font.SysFont('arial',30)
        score=font.render(f"Score : {self.snake.length}",True,(255,255,255))
        self.surface.blit(score,(850,10))
        pygame.display.flip()

    def set_background(self):
        bg=pygame.image.load("resources/background.jpg")
        self.surface.blit(bg,(0,0))

    #collision with apple
    def is_collision(self,x1,y1,x2,y2):
        if x1>=x2 and x1<x2+SIZE:
            if y1>=y2 and y1<y2+SIZE:
                return True
        return False

    def show_game_over(self):
        self.set_background()
        font=pygame.font.SysFont('arial',30)
        line1=font.render(f"Game Over : Your score is {self.snake.length}",True,(255,255,255))
        self.surface.blit(line1,(200,300))
        line1=font.render("To paly again press Enter , To exit press Escape",True,(255,255,255))
        self.surface.blit(line1,(200,340))
        pygame.display.flip()
        pygame.mixer.music.pause()
        
    def reset(self):
        self.snake=Snake(self.surface,1)
        self.apple=Apple(self.surface)

    def move_apple(self):
        self.apple.x=random.randint(1,24)*SIZE
        self.apple.y=random.randint(1,14)*SIZE

    def play(self):
        self.set_background()
        self.snake.walk()
        self.apple.draw()
        self.score_display()
        self.snake.x[0]=self.snake.x[0]%1000
        self.snake.y[0]=self.snake.y[0]%600

        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.play_sound("resources/ding.mp3")
            self.increase_length()
            self.move_apple()
        for i in range(2,self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                self.play_sound("resources/crash.mp3")
                raise "Game Over"


    def run(self):
        # we will use infinte loop for event and action will be taken accordingly
        running=True
        pause=False
        while running:
            for event in pygame.event.get():      #pygame.event.get() brings every event  or get events from the queue
                if event.type == KEYDOWN:
                    if event.key==K_ESCAPE:
                        running=False
                    if event.key==K_RETURN:
                        pause=False
                        pygame.mixer.music.unpause()

                    if event.key==K_UP:
                        self.snake.move_up()             #decrease the value of y if you are pressing up button to go up
                        
                    if event.key==K_DOWN:
                        self.snake.move_down()
                    if event.key==K_LEFT:
                        self.snake.move_left()
                    if event.key==K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:              # QUIT is when cross(cancel) button of window, KEYDOWN and Quit is constant and import using from pygame.locals import *
                    running=False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause=True
                self.reset()
            time.sleep(.2)              #decrease sleep time to increase speed up
