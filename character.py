import pygame

class Character():
    def __init__(self, x, y, img, gender):
        self.image = pygame.image.load(img).convert_alpha()
        #self.image = pygame.transform.scale(self.image, (50,75)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.gender=gender
        self.position=0
        self.bgPic="heart1.gif"

    def moveAhead(self):
        self.position+=1
        if(self.position==0):
            self.bgPic="heart1.gif"
            self.rect.x=450
            self.rect.y=70
        if(self.position==1):
            self.bgPic="heart11.gif"
            self.rect.x=275
            self.rect.y=0
        if(self.position==2):
            self.bgPic="heart12.gif"
            self.rect.x=75
            self.rect.y=275
        if(self.position==3):
            self.bgPic="heart13.gif"
            self.rect.x=450
            self.rect.y=615
        if(self.position==4):
            self.bgPic="heart14.gif"
            self.rect.x=860
            self.rect.y=275
        if(self.position==5):
            self.bgPic="heart15.gif"
            self.rect.x=620
            self.rect.y=0
        #if(self.position==1)


'''
    def moveAhead(self):
        self.postion++
        if(self.postion==1):
            self.rect.x=300
            self.rect.y=50


        elif(self.postion==2):
            self.rect.x=50
            self.rect.y=300
        elif(self.postion==3):
            self.rect.x=300
            self.rect.y=500
        elif(self.postion==4):
            self.rect.x=600
            self.rect.y=300
        elif(self.postion==5):
            self.rect.x=50
            self.rect.y=100
        elif(self.postion==6):
            self.rect.x=420
            self.rect.y=100
            '''
