import pygame 
import random
import math
from pygame import mixer
#Здрвствуйте, ввиду того что у меня сейчас послдение экзамены не смог уделять достаточно времени для задачи, поэтому сделал только часть задания, но хотелось бы получить обратную связь по ней, чтобы понять что я делаю не так и как это исправить. Спасибо!
#Я использовал библиотеку pygame, так как она позволяет создавать игры и работать с графикой, что мне показалось наиболее подходящим для данной задачи.
#Логика которуя я придумал для столкновении не работает, выдает много ошибок, думаю есть какой нибудь метод проще, но не придумал(
#Добавил комментарии на английском, мне так было легче писать, надеюсь это не проблема

#initializing game and display
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("nFactorial: Rock-Paper-Scissors WAR!!!")
#setting backfround image
backgroung = pygame.image.load('arena.jpg')
#setting background music
mixer.music.load('cupid.mp3')
mixer.music.play(-1)
#to randomize the directions of objects
directions = [-1,1]
#created a class for all Rocks, Papers and Scissors
class Warrior():
    def __init__(self,type):
        self.type = type
        #images are 50x50 pixels so the random position is set accordingly
        self.pos_x = random.randint(0,750)
        self.pos_y = random.randint(0,550)
        self.dir_x = random.choice(directions)
        self.dir_y = random.choice(directions)
    #based on type diffrent images are loaded    
    def type_rock(self):
        self.image = pygame.image.load('rock.png')
    def type_paper(self):
        self.image = pygame.image.load('paper.png')
    def type_scissors(self):
        self.image = pygame.image.load('scissors.png')
    def move(self):
        #movement of objects
        self.pos_x += self.dir_x * 0.1
        self.pos_y += self.dir_y * 0.1
        isBorder(self,self.pos_x,self.pos_y)
    def draw(self):
        #drawing objects
        screen.blit(self.image,(self.pos_x,self.pos_y))
    def type(self):
        return self.type
class War():
    #Here I tried to create a class for actions between objects, however did not manage to solve problem with collisions
    def __init__(self):
        self.number_of_rocks = random.randint(5,10)
        self.rocks = {}
        for i in range(self.number_of_rocks):
            self.rocks[i] = Warrior('rock')
            self.rocks[i].type_rock()
        self.number_of_papers = random.randint(5,10)
        self.papers = {}
        for i in range(self.number_of_papers):
            self.papers[i] = Warrior('paper')
            self.papers[i].type_paper()
        self.number_of_scissors = random.randint(5,10)
        self.scissors = {}
        for i in range(self.number_of_scissors):
            self.scissors[i] = Warrior('scissors')
            self.scissors[i].type_scissors()
    #drawing of every object and type and moving it
    def draw(self):
        for i in range(self.number_of_rocks):
            self.rocks[i].draw()
            self.rocks[i].move()
        for i in range(self.number_of_papers):
            self.papers[i].draw()
            self.papers[i].move()
        for i in range(self.number_of_scissors):
            self.scissors[i].draw()
            self.scissors[i].move()
    #collision between objects, calculated by mathematical formula, distance is 51 because images are 50x50 pixels
    def isCollision(self,x1,y1,x2,y2):
        distance = math.sqrt((math.pow(x1-x2,2))+(math.pow(y1-y2,2)))
        if distance < 51:
            return True
        else:
            return False
    '''
    def collision(self):
        for i in range(self.number_of_rocks):
            for j in range(self.number_of_papers):
                if self.isCollision(self.rocks[i].pos_x,self.rocks[i].pos_y,self.papers[j].pos_x,self.papers[j].pos_y):
                    self.number_of_rocks -= 1
                    self.number_of_papers += 1
                    self.papers[self.number_of_papers] = Warrior('paper')
                    self.papers[self.number_of_papers].pos_x = self.rocks[i].pos_x
                    self.papers[self.number_of_papers].pos_y = self.rocks[i].pos_y
                    del self.rocks[i]
        for i in range(self.number_of_rocks):
            for j in range(self.number_of_scissors):
                if self.isCollision(self.rocks[i].pos_x,self.rocks[i].pos_y,self.scissors[j].pos_x,self.scissors[j].pos_y):
                    self.number_of_rocks += 1
                    self.number_of_scissors -= 1
                    self.rocks[self.number_of_rocks] = Warrior('rocks')
                    self.rocks[self.number_of_rocks].pos_x = self.scissors[j].pos_x
                    self.rocks[self.number_of_rocks].pos_y = self.scissors[j].pos_y
                    del self.rocks[j]
        '''

#if objects hits border it will bounce back            
def isBorder(object,pos_x, pos_y):
    if pos_x <= 0 or pos_x >= 750:
        object.dir_x *= -1
    if pos_y <= 0 or pos_y >= 550:
        object.dir_y *= -1


#Game
game = War()
running = True
while running:
    screen.blit(backgroung,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    game.draw()
    pygame.display.update()